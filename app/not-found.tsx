'use client'

import Link from '@/components/Link'

import { usePathname, redirect } from 'next/navigation'

// Legacy paths from seanbmcgregor.com
const redirects = {
  '/SafetyJekyll': '/blog/jekyll',
  '/ProblemOfPriors': '/blog/priors',
  '/unit-testing-social-good': '/blog/unit-testing-algorithms-for-social-good',
  '/SustainableDevelopment': '/blog/Sustainable-Development-Goals',
  '/color-selection-game': '/blog/color-selection-game',
  '/Starship': '/blog/anatomy-of-an-incident',
  '/cryptographic-thinking': '/blog/cryptographic-thinking',
  '/visualization-for-mdps': '/blog/visualization-for-mdps',
  '/should-i-change-my-password': '/blog/should-i-change-my-password',
  '/SelfDrivingCars': '/blog/self-driving-car',
  '/compromising-combination-bike-locks': '/blog/compromising-combination-bike-locks',
  '/securing-user-content-in-the-javascriptable-web':
    '/blog/securing-user-content-in-the-javascriptable-web',
  '/SyntiantCore2': '/blog/syntiant-core-2',
  '/hcaibook': '/blog/hcai.mdx:slug: hcaibook',
  '/DeepfakeDetectionGame': '/blog/deepfake-cat-and-mouse',
  '/MyAISummer': '/blog/my-ai-summer',
  '/DeepQVisualization': '/blog/breakout',
  '/hacking-a-url-shortener-into-a-comment-system':
    '/blog/hacking-a-url-shortener-into-a-comment-system',
  '/EthicsSafetySchism': '/blog/schism.mdx',
  '/AmazonFresh': '/blog/amazon-fresh',
  '/vlhcc2015': '/blog/vlhcc2015',
}

export default function NotFound() {
  const pathname = usePathname()

  if (pathname in redirects) {
    redirect(redirects[pathname])
  }

  if (pathname.startsWith('/tag/')) {
    redirect(pathname.replace('/tag/', '/tags/').replace('.html', ''))
  }

  if (pathname.startsWith('/archives.html')) {
    redirect('/blog')
  }

  if (pathname.startsWith('/pages/about.html')) {
    redirect('/about')
  }

  if (pathname.startsWith('/pages/vitae.html')) {
    redirect('/about')
  }

  if (pathname.startsWith('/papers/')) {
    redirect('/static' + pathname)
  }

  return (
    <div className="flex flex-col items-start justify-start md:mt-24 md:flex-row md:items-center md:justify-center md:space-x-6">
      <div className="space-x-2 pb-8 pt-6 md:space-y-5">
        <h1 className="text-6xl font-extrabold leading-9 tracking-tight text-gray-900 dark:text-gray-100 md:border-r-2 md:px-6 md:text-8xl md:leading-14">
          404
        </h1>
      </div>
      <div className="max-w-md">
        <p className="mb-4 text-xl font-bold leading-normal md:text-2xl">
          Sorry we couldn't find this page.
        </p>
        <p className="mb-8">
          But don't worry, you can find plenty of other things on the homepage.
        </p>
        <Link
          href="/"
          className="focus:shadow-outline-blue inline rounded-lg border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium leading-5 text-white shadow transition-colors duration-150 hover:bg-blue-700 focus:outline-none dark:hover:bg-blue-500"
        >
          Back to homepage
        </Link>
      </div>
    </div>
  )
}
