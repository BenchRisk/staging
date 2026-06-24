#!/usr/bin/env python3
"""Score a BenchRisk benchmark against the mitigation rubrics via OpenRouter.

Pipeline:
  1. Open a score file from data/scores/ (by name or path).
  2. Loop through the mitigation rubric prompts in data/langfuse/mitigations_rubrics/.
  3. Compose each rubric (shared Component 1 + mitigation Component 2) with the
     benchmark's name and documents, and send it to a model via OpenRouter.
  4. Parse each verdict, update the score file's `adoptedMitigations` /
     `absentMitigations` lists, set `scoredBy` (default `machine`; see --scored-by), and
     set `dateScored` to today (use --keep-date to skip).

The "documents" handed to the model are assembled from the score file itself — its
`benchmarkDescription`, `references`, and markdown body — i.e., what the repo knows about
the benchmark. The existing mitigation lists are deliberately NOT included, so prior
scoring cannot bias the model. Use --documents-file to grade against external material
(e.g., the benchmark's paper/README) instead.

With --fetch-references the reference URLs are retrieved and their full text appended to
the documents: arXiv /abs/ links are fetched as PDFs and extracted to full text; other
pages are fetched and reduced to readable text. Retrievals are cached on disk (default
<repo>/.cache/references) and are not re-fetched while present (use --refresh-cache to
force; failures are never cached). PDF text extraction prefers PyMuPDF, then pdfminer.six,
then pypdf — install one into a local venv, e.g.
`uv venv .venv && uv pip install --python .venv/bin/python -r seeding/requirements.txt`.

Verdict -> list mapping (default):
    adopted               -> adoptedMitigations
    partially_adopted     -> absentMitigations
    absent                -> absentMitigations
    insufficient_evidence -> absentMitigations  (or left unchanged with --skip-insufficient)
Use --threshold T to instead decide by the model's `likelihood` (>= T -> adopted).

Logging: every OpenRouter request attempt (success, API/HTTP error, retry, connection
failure) is appended to llm.log (default <repo>/llm.log; override with --log-file, add
the request body with --log-requests, disable with --no-log). Each record holds the full
response payload — id, model, choices/content, finish_reason, usage, cost — so you can
inspect exactly what the hosted model did. (llm.log matches *.log in .gitignore.)

Configuration (env, also read from the repo .env if present and not already set):
    OPENROUTER_API_KEY   (required unless --dry-run)
    OPENROUTER_BASE_URL  (optional; default https://openrouter.ai/api/v1)

Examples:
    # Dry run: compose prompts, call nothing, write nothing
    python seeding/score_benchmark.py --score MMLU --dry-run

    # Score three specific mitigations with the default model and write the result
    python seeding/score_benchmark.py --score MMLU --mitigations 1,2,57

    # Score a range with a chosen model, report only (no file write)
    python seeding/score_benchmark.py --score data/scores/HumanEval.mdx \
        --mitigations 1-20 --model openai/gpt-4o --no-write

    # Fetch & cache the full reference texts (arXiv PDF, MLCommons page), then dry-run
    python seeding/score_benchmark.py --score AILuminate10 --mitigations 1 \
        --fetch-references --dry-run

No third-party packages required (standard library only).
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import io
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCORES_DIR = REPO_ROOT / "data" / "scores"
RUBRIC_DIR = REPO_ROOT / "data" / "langfuse" / "mitigations_rubrics"
ENV_FILE = REPO_ROOT / ".env"
DEFAULT_MODEL = "anthropic/claude-sonnet-4.5"
DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_CACHE_DIR = REPO_ROOT / ".cache" / "references"
FETCH_USER_AGENT = "BenchRisk-reference-fetcher/1.0 (+https://github.com/BenchRisk/BenchRisk)"

MIT_FILE_RE = re.compile(r"^mitigation\.(\d+)\.prompt\.md$")
ADOPTED_FIELD = "adoptedMitigations"
ABSENT_FIELD = "absentMitigations"


# --------------------------------------------------------------------------- env / io
def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def strip_comments(text: str) -> str:
    """Remove HTML maintenance comments so prompts sent to the model stay clean."""
    text = re.sub(r"<!--.*?-->\n*", "", text, flags=re.S)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def resolve_score_path(score: str) -> Path:
    p = Path(score)
    if p.exists():
        return p
    cand = SCORES_DIR / (score if score.endswith(".mdx") else f"{score}.mdx")
    if cand.exists():
        return cand
    sys.exit(f"Score file not found: {score} (looked in {SCORES_DIR})")


# --------------------------------------------------------------------------- frontmatter
def split_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        sys.exit("Score file has no YAML frontmatter.")
    return m.group(1), m.group(2)


def get_scalar(fm: str, field: str) -> str:
    lines = fm.split("\n")
    for idx, line in enumerate(lines):
        m = re.match(rf"^{re.escape(field)}:\s*(.*)$", line)
        if m:
            parts = [m.group(1)]
            j = idx + 1
            while j < len(lines) and (lines[j].startswith(" ") or lines[j].startswith("\t")):
                parts.append(lines[j].strip())
                j += 1
            return " ".join(parts).strip().strip("'").strip('"')
    return ""


def get_list(fm: str, field: str) -> list[int]:
    lines = fm.split("\n")
    i, n, vals = 0, len(fm.split("\n")), []
    while i < n:
        if re.match(rf"^{re.escape(field)}:\s*(.*)$", lines[i]):
            inline = re.match(rf"^{re.escape(field)}:\s*\[(.*)\]\s*$", lines[i])
            if inline:
                return [int(x) for x in re.findall(r"-?\d+", inline.group(1))]
            i += 1
            while i < n and not re.match(r"^[A-Za-z0-9_]+\s*:", lines[i]):
                mm = re.match(r"^\s*-\s*(\d+)", lines[i])
                if mm:
                    vals.append(int(mm.group(1)))
                i += 1
            return vals
        i += 1
    return vals


def get_str_list(fm: str, field: str) -> list[str]:
    """Read a top-level block (or inline) list of string values from the frontmatter."""
    lines = fm.split("\n")
    i, n, vals = 0, len(lines), []
    while i < n:
        if re.match(rf"^{re.escape(field)}:\s*(.*)$", lines[i]):
            inline = re.match(rf"^{re.escape(field)}:\s*\[(.*)\]\s*$", lines[i])
            if inline:
                return [x.strip().strip("'").strip('"')
                        for x in inline.group(1).split(",") if x.strip()]
            i += 1
            while i < n and not re.match(r"^[A-Za-z0-9_]+\s*:", lines[i]):
                mm = re.match(r"^\s*-\s*(.*)$", lines[i])
                if mm and mm.group(1).strip():
                    vals.append(mm.group(1).strip().strip("'").strip('"'))
                i += 1
            return vals
        i += 1
    return vals


def set_block_list(fm: str, field: str, values: list[int]) -> str:
    """Replace a top-level block-list field's values, leaving all other text intact."""
    lines = fm.split("\n")
    out, i, n, replaced = [], 0, len(lines), False
    block = [f"{field}:"] + [f"  - {v}" for v in values] if values else [f"{field}: []"]
    while i < n:
        if re.match(rf"^{re.escape(field)}:\s*(.*)$", lines[i]):
            out.extend(block)
            replaced = True
            i += 1
            while i < n and not re.match(r"^[A-Za-z0-9_]+\s*:", lines[i]):
                i += 1
            continue
        out.append(lines[i])
        i += 1
    if not replaced:
        out.extend(block)
    return "\n".join(out)


# --------------------------------------------------------------------------- rubric / docs
def parse_mitigation_spec(spec: str) -> list[int]:
    out: set[int] = set()
    for part in spec.replace(" ", "").split(","):
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return sorted(out)


def available_mitigations() -> list[int]:
    nums = []
    for p in RUBRIC_DIR.glob("mitigation.*.prompt.md"):
        m = MIT_FILE_RE.match(p.name)
        if m:
            nums.append(int(m.group(1)))
    return sorted(nums)


def assemble_documents(name: str, fm: str, body: str) -> str:
    desc = get_scalar(fm, "benchmarkDescription")
    refs = get_str_list(fm, "references")
    parts = [f"# Benchmark: {name}", ""]
    if desc:
        parts += ["## Description", desc, ""]
    if refs:
        parts += ["## References", "\n".join(f"- {r}" for r in refs), ""]
    if body.strip():
        parts += ["## Documentation", body.strip(), ""]
    return "\n".join(parts).strip() + "\n"


def compile_prompt(shared: str, mitigation: str, benchmark_name: str, documents: str) -> str:
    """Fill the shared scaffold. Insert documents LAST so braces in docs aren't expanded."""
    out = shared.replace("{{mitigation_rubric}}", mitigation)
    out = out.replace("{{benchmark_name}}", benchmark_name)
    out = out.replace("{{documents}}", documents)
    return out


# --------------------------------------------------------------------------- references
class _HTMLTextExtractor(HTMLParser):
    """Collect visible text from an HTML page, skipping script/style/etc."""

    _SKIP = {"script", "style", "noscript", "svg", "head"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self._skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self._SKIP:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self._SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            t = data.strip()
            if t:
                self.parts.append(t)


def html_to_text(html_str: str) -> str:
    parser = _HTMLTextExtractor()
    try:
        parser.feed(html_str)
    except Exception:  # noqa: BLE001 - tolerate malformed markup
        pass
    return re.sub(r"\n{3,}", "\n\n", "\n".join(parser.parts)).strip()


def extract_pdf_text(data: bytes) -> str:
    """Full-text extraction, preferring PyMuPDF, then pdfminer.six, then pypdf."""
    try:
        import pymupdf  # PyMuPDF >= 1.24
        doc = pymupdf.open(stream=data, filetype="pdf")
        try:
            return "\n".join(page.get_text() for page in doc)
        finally:
            doc.close()
    except ImportError:
        pass
    try:
        import fitz  # older PyMuPDF import name
        doc = fitz.open(stream=data, filetype="pdf")
        try:
            return "\n".join(page.get_text() for page in doc)
        finally:
            doc.close()
    except ImportError:
        pass
    try:
        from pdfminer.high_level import extract_text
        return extract_text(io.BytesIO(data))
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(data))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    except ImportError:
        pass
    raise RuntimeError(
        "no PDF backend available — install one into your environment, e.g. "
        "`uv pip install --python .venv/bin/python pymupdf`")


def normalize_fetch_url(url: str) -> str:
    """Map an arXiv abstract page to its PDF so we retrieve full text."""
    m = re.match(r"^(https?://arxiv\.org)/abs/(.+)$", url.strip())
    if m:
        return f"{m.group(1)}/pdf/{m.group(2)}"
    return url.strip()


def fetch_url(url: str, timeout: int = 60):
    """Return (kind, text) for a URL; kind is one of {'pdf', 'html', 'text'}."""
    target = normalize_fetch_url(url)
    req = urllib.request.Request(
        target, headers={"User-Agent": FETCH_USER_AGENT, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        ctype = (resp.headers.get("Content-Type") or "").lower()
        raw = resp.read()
    if "application/pdf" in ctype or target.lower().endswith(".pdf") or raw[:5] == b"%PDF-":
        return "pdf", extract_pdf_text(raw)
    if "html" in ctype or raw.lstrip()[:1] == b"<":
        return "html", html_to_text(raw.decode("utf-8", "replace"))
    return "text", raw.decode("utf-8", "replace")


def fetch_references(refs, cache_dir: Path, timeout: int = 60, refresh: bool = False):
    """Fetch each reference URL, caching successful extractions on disk.

    A reference already present in the cache is NOT re-fetched (unless refresh=True).
    Failures are not cached, so they are retried on the next run. Returns result dicts.
    """
    cache_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for url in refs:
        key = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
        txt_path = cache_dir / f"{key}.txt"
        meta_path = cache_dir / f"{key}.json"
        if not refresh and txt_path.exists():
            text = txt_path.read_text(encoding="utf-8")
            print(f"  CACHED  {url}  ({len(text)} chars)")
            results.append({"url": url, "status": "cached", "text": text})
            continue
        try:
            kind, text = fetch_url(url, timeout=timeout)
            text = text.strip()
            txt_path.write_text(text, encoding="utf-8")
            meta_path.write_text(json.dumps(
                {"url": url, "kind": kind, "chars": len(text),
                 "fetched_at": datetime.now(timezone.utc).isoformat()},
                indent=2), encoding="utf-8")
            print(f"  FETCHED {url}  [{kind}, {len(text)} chars]")
            results.append({"url": url, "status": "fetched", "kind": kind, "text": text})
        except Exception as e:  # noqa: BLE001 - report and continue with other refs
            print(f"  FAILED  {url}  ({e})")
            results.append({"url": url, "status": "failed", "error": str(e), "text": ""})
    return results


def render_fetched_section(fetched, max_chars: int = 0) -> str:
    """Append fetched reference texts to the documents (optionally truncated each)."""
    out = ["", "## Fetched reference contents", ""]
    for r in fetched:
        if r["status"] == "failed":
            out += [f"### Source: {r['url']}",
                    f"(could not retrieve: {r.get('error', '')})", ""]
            continue
        text = r["text"]
        note = ""
        if max_chars and len(text) > max_chars:
            text, note = text[:max_chars], f" (truncated to {max_chars} chars)"
        out += [f"### Source: {r['url']}{note}", text, ""]
    return "\n".join(out)


# --------------------------------------------------------------------------- openrouter
def extract_json(content: str):
    s = content.strip()
    if s.startswith("```"):
        s = re.sub(r"^```[a-zA-Z]*\n", "", s)
        s = re.sub(r"\n```$", "", s).strip()
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        pass
    start = s.find("{")
    if start < 0:
        return None
    depth = 0
    for i in range(start, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(s[start:i + 1])
                except json.JSONDecodeError:
                    return None
    return None


class LlmLogger:
    """Thread-safe append logger capturing the full OpenRouter API exchange.

    One record is written per request attempt — successes, API errors, HTTP errors,
    non-JSON bodies, and connection failures alike — so the log shows everything the
    hosted model returned (id, model, choices/content, finish_reason, usage, cost, ...).
    """

    def __init__(self, path: Path, enabled: bool = True, log_requests: bool = False):
        self.path = path
        self.enabled = enabled
        self.log_requests = log_requests
        self._lock = threading.Lock()

    def _write(self, text: str) -> None:
        with self._lock:
            with open(self.path, "a", encoding="utf-8") as f:
                f.write(text)

    def session(self, **fields) -> None:
        if not self.enabled:
            return
        ts = datetime.now(timezone.utc).isoformat()
        meta = "  ".join(f"{k}={v}" for k, v in fields.items())
        self._write(f"\n{'#' * 80}\n# SESSION {ts}  {meta}\n{'#' * 80}\n")

    def record(self, *, benchmark: str, mitigation, model: str, status: str,
               attempt=None, payload=None, request=None, error=None) -> None:
        if not self.enabled:
            return
        ts = datetime.now(timezone.utc).isoformat()
        header = (f"{ts} | benchmark={benchmark} | mitigation={mitigation} "
                  f"| model={model} | status={status}")
        if attempt is not None:
            header += f" | attempt={attempt}"
        parts = ["=" * 80, header, "-" * 80]
        if request is not None and self.log_requests:
            parts += ["REQUEST:", json.dumps(request, indent=2, ensure_ascii=False), "-" * 80]
        if payload is not None:
            parts += ["RESPONSE:", json.dumps(payload, indent=2, ensure_ascii=False)]
        if error is not None:
            parts += ["ERROR:", str(error)]
        parts.append("=" * 80 + "\n")
        self._write("\n".join(parts) + "\n")


def call_openrouter(base_url: str, api_key: str, model: str, prompt: str,
                    temperature: float, max_tokens: int, json_mode: bool,
                    retries: int = 3, timeout: int = 120,
                    logger: "LlmLogger | None" = None,
                    benchmark: str = "", mitigation=""):
    url = base_url.rstrip("/") + "/chat/completions"
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if json_mode:
        body["response_format"] = {"type": "json_object"}
    data = json.dumps(body).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/BenchRisk/BenchRisk",
        "X-Title": "BenchRisk Mitigation Scoring",
    }

    def log(status, attempt, payload=None, error=None):
        if logger:
            # Never log the auth header; the request body carries no secrets.
            logger.record(benchmark=benchmark, mitigation=mitigation, model=model,
                          status=status, attempt=attempt, payload=payload,
                          request=body, error=error)

    last_err = None
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=data, method="POST")
        for k, v in headers.items():
            req.add_header(k, v)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw_text = resp.read().decode("utf-8", "replace")
            try:
                payload = json.loads(raw_text)
            except json.JSONDecodeError:
                last_err = "non-JSON response from API"
                log("non_json", attempt, error=raw_text[:5000])
                if attempt < retries:
                    time.sleep(2 ** attempt)
                    continue
                return None, last_err
            if isinstance(payload, dict) and payload.get("error"):
                log("api_error", attempt, payload=payload)
                return None, f"API error: {payload['error']}"
            log("ok", attempt, payload=payload)
            try:
                content = payload["choices"][0]["message"]["content"]
            except (KeyError, IndexError, TypeError) as e:
                return None, f"unexpected response shape: {e}"
            return content, None
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")
            last_err = f"HTTP {e.code}: {detail[:300]}"
            log("http_error", attempt, error=f"HTTP {e.code}: {detail}")
            if e.code in (408, 409, 425, 429, 500, 502, 503, 504) and attempt < retries:
                time.sleep(2 ** attempt)
                continue
            return None, last_err
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = f"connection error: {e}"
            log("connection_error", attempt, error=str(e))
            if attempt < retries:
                time.sleep(2 ** attempt)
                continue
            return None, last_err
    return None, last_err


# --------------------------------------------------------------------------- decision
def decide(result: dict | None, threshold: float | None, skip_insufficient: bool) -> str:
    """Return 'adopted', 'absent', 'skip', or 'error'."""
    if result is None:
        return "error"
    verdict = str(result.get("verdict", "")).strip().lower()
    likelihood = result.get("likelihood")
    if threshold is not None and isinstance(likelihood, (int, float)):
        return "adopted" if likelihood >= threshold else "absent"
    if verdict == "adopted":
        return "adopted"
    if verdict == "insufficient_evidence" and skip_insufficient:
        return "skip"
    if verdict in ("absent", "partially_adopted", "insufficient_evidence"):
        return "absent"
    # Unknown/missing verdict: be conservative.
    return "absent"


# --------------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--score", required=True,
                    help="score file name (e.g. MMLU) or path under data/scores/")
    ap.add_argument("--mitigations", default=None,
                    help="comma list / ranges, e.g. '1,2,57' or '1-20,57'. Default: all")
    ap.add_argument("--model", default=DEFAULT_MODEL,
                    help=f"OpenRouter model id (default: {DEFAULT_MODEL})")
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--max-tokens", type=int, default=2000)
    ap.add_argument("--json-mode", action="store_true",
                    help="request response_format=json_object (model must support it)")
    ap.add_argument("--threshold", type=float, default=None,
                    help="decide by model likelihood >= T instead of by verdict")
    ap.add_argument("--skip-insufficient", action="store_true",
                    help="leave 'insufficient_evidence' mitigations unchanged")
    ap.add_argument("--workers", type=int, default=4, help="concurrent requests")
    ap.add_argument("--documents-file", default=None,
                    help="use this file's contents as the documents instead of the score file")
    ap.add_argument("--fetch-references", action="store_true",
                    help="fetch each reference URL (arXiv PDFs -> full text, pages -> text) "
                         "and append it to the documents")
    ap.add_argument("--cache-dir", default=None,
                    help=f"reference fetch cache directory (default: {DEFAULT_CACHE_DIR})")
    ap.add_argument("--refresh-cache", action="store_true",
                    help="re-fetch references even if already cached")
    ap.add_argument("--fetch-timeout", type=int, default=60,
                    help="per-URL fetch timeout in seconds (default 60)")
    ap.add_argument("--max-ref-chars", type=int, default=0,
                    help="truncate each fetched reference to N chars (0 = full text)")
    ap.add_argument("--keep-date", action="store_true",
                    help="leave dateScored unchanged (by default it is set to today on write)")
    ap.add_argument("--scored-by", choices=["machine", "human", "maintainer"], default="machine",
                    help="value written to scoredBy (default: machine — a machine annotation "
                         "without full human review)")
    ap.add_argument("--api-key", default=None, help="env OPENROUTER_API_KEY")
    ap.add_argument("--base-url", default=None, help="env OPENROUTER_BASE_URL")
    ap.add_argument("--log-file", default=None,
                    help="append full OpenRouter responses here (default: <repo>/llm.log)")
    ap.add_argument("--log-requests", action="store_true",
                    help="also log each request body (includes the full composed prompt)")
    ap.add_argument("--no-log", action="store_true",
                    help="disable writing the llm.log file")
    ap.add_argument("--no-write", action="store_true",
                    help="call the model but do not modify the score file")
    ap.add_argument("--dry-run", action="store_true",
                    help="compose prompts only; call nothing and write nothing")
    args = ap.parse_args()

    load_dotenv(ENV_FILE)
    base_url = args.base_url or os.environ.get("OPENROUTER_BASE_URL") or DEFAULT_BASE_URL
    api_key = args.api_key or os.environ.get("OPENROUTER_API_KEY")
    log_path = Path(args.log_file) if args.log_file else REPO_ROOT / "llm.log"
    cache_dir = Path(args.cache_dir) if args.cache_dir else DEFAULT_CACHE_DIR

    score_path = resolve_score_path(args.score)
    raw = score_path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(raw)
    name = get_scalar(fm, "name") or score_path.stem

    shared_path = RUBRIC_DIR / "shared.prompt.md"
    if not shared_path.exists():
        sys.exit(f"Shared rubric component not found: {shared_path}")
    shared = strip_comments(shared_path.read_text(encoding="utf-8"))

    if args.documents_file:
        documents = Path(args.documents_file).read_text(encoding="utf-8")
    else:
        documents = assemble_documents(name, fm, body)
        if args.fetch_references:
            refs = get_str_list(fm, "references")
            print(f"Fetching {len(refs)} reference(s) into {cache_dir} ...")
            fetched = fetch_references(refs, cache_dir, timeout=args.fetch_timeout,
                                       refresh=args.refresh_cache)
            documents += render_fetched_section(fetched, args.max_ref_chars)
            print("-" * 78)

    requested = parse_mitigation_spec(args.mitigations) if args.mitigations else available_mitigations()
    targets = []
    missing = []
    for num in requested:
        p = RUBRIC_DIR / f"mitigation.{num:03d}.prompt.md"
        if p.exists():
            targets.append((num, p))
        else:
            missing.append(num)

    print(f"Benchmark   : {name}  ({score_path.relative_to(REPO_ROOT)})")
    print(f"Model       : {args.model}")
    print(f"Mitigations : {len(targets)} to assess" +
          (f"  (missing rubric files: {missing})" if missing else ""))
    print(f"Documents   : {len(documents)} chars"
          + (f"  (from {args.documents_file})" if args.documents_file else "  (from score file)"))
    print(f"Log         : {'(disabled)' if args.no_log else log_path}")
    print("-" * 78)

    if not targets:
        sys.exit("No rubric files to assess.")

    if args.dry_run:
        num, p = targets[0]
        composed = compile_prompt(shared, strip_comments(p.read_text(encoding="utf-8")),
                                  name, documents)
        print(f"DRY RUN — would assess mitigations: {[n for n, _ in targets]}")
        print(f"\n----- composed prompt for mitigation {num} "
              f"({len(composed)} chars), preview -----\n")
        print(composed[:12800])
        print("\n... [truncated] ...")
        return 0

    if not api_key:
        sys.exit("Missing OPENROUTER_API_KEY (env, .env, or --api-key).")

    logger = LlmLogger(log_path, enabled=not args.no_log, log_requests=args.log_requests)
    logger.session(benchmark=name, model=args.model, mitigations=len(targets),
                   score_file=str(score_path.relative_to(REPO_ROOT)),
                   base_url=base_url, temperature=args.temperature)

    def assess(item):
        num, p = item
        mitigation = strip_comments(p.read_text(encoding="utf-8"))
        prompt = compile_prompt(shared, mitigation, name, documents)
        content, err = call_openrouter(base_url, api_key, args.model, prompt,
                                        args.temperature, args.max_tokens, args.json_mode,
                                        logger=logger, benchmark=name, mitigation=num)
        if err:
            return num, None, err
        return num, extract_json(content), (None if content else "empty response")

    results: dict[int, dict | None] = {}
    errors: dict[int, str] = {}
    with cf.ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        for num, result, err in ex.map(assess, targets):
            results[num] = result
            if err and result is None:
                errors[num] = err

    # Decide and report
    decisions: dict[int, str] = {}
    print(f"{'mit':>4}  {'verdict':<20} {'like':>5} {'conf':>5}  -> decision")
    for num, _ in targets:
        res = results.get(num)
        d = decide(res, args.threshold, args.skip_insufficient)
        decisions[num] = d
        if num in errors:
            print(f"{num:>4}  {'ERROR':<20} {'':>5} {'':>5}  -> {errors[num][:60]}")
            continue
        verdict = (res or {}).get("verdict", "?")
        like = (res or {}).get("likelihood", "")
        conf = (res or {}).get("confidence", "")
        like_s = f"{like:.2f}" if isinstance(like, (int, float)) else ""
        conf_s = f"{conf:.2f}" if isinstance(conf, (int, float)) else ""
        print(f"{num:>4}  {str(verdict):<20} {like_s:>5} {conf_s:>5}  -> {d}")

    # Update the two lists (move + dedupe), preserving order of untouched entries
    adopted = get_list(fm, ADOPTED_FIELD)
    absent = get_list(fm, ABSENT_FIELD)
    changed = 0
    for num, d in decisions.items():
        if d in ("adopted", "absent"):
            adopted = [x for x in adopted if x != num]
            absent = [x for x in absent if x != num]
            (adopted if d == "adopted" else absent).append(num)
            changed += 1

    n_adopted = sum(1 for d in decisions.values() if d == "adopted")
    n_absent = sum(1 for d in decisions.values() if d == "absent")
    n_skip = sum(1 for d in decisions.values() if d == "skip")
    n_err = len(errors)
    print("-" * 78)
    print(f"adopted={n_adopted}  absent={n_absent}  skipped={n_skip}  errors={n_err}")

    if args.no_write:
        print("--no-write: score file not modified.")
        return 1 if n_err else 0

    new_fm = set_block_list(fm, ADOPTED_FIELD, adopted)
    new_fm = set_block_list(new_fm, ABSENT_FIELD, absent)
    # Record provenance: a machine run produces machine annotations unless told otherwise.
    new_fm, n_sb = re.subn(r"(?m)^scoredBy:.*$", f"scoredBy: {args.scored_by}", new_fm)
    if n_sb == 0:  # field absent — add it right after name:
        new_fm = re.sub(r"(?m)^(name:.*\n)", rf"\1scoredBy: {args.scored_by}\n", new_fm, count=1)
    date_note = ""
    if not args.keep_date:
        today = date.today().isoformat()
        new_fm, n_sub = re.subn(r"(?m)^dateScored:.*$", f"dateScored: '{today}'", new_fm)
        if n_sub == 0:  # field absent for some reason — add it
            new_fm = new_fm.rstrip("\n") + f"\ndateScored: '{today}'"
        date_note = f"; dateScored set to {today}"
    score_path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")
    print(f"Updated {score_path.relative_to(REPO_ROOT)} "
          f"({changed} mitigations placed; scoredBy={args.scored_by}, adopted list={len(adopted)}, "
          f"absent list={len(absent)}{date_note}).")
    return 1 if n_err else 0


if __name__ == "__main__":
    raise SystemExit(main())
