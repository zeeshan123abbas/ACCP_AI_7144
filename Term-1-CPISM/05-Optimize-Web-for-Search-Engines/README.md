# 05 · Optimize Web for Search Engines (SEO)

![Google Search Console](https://img.shields.io/badge/Google_Search_Console-458CF5?style=for-the-badge&logo=googlesearchconsole&logoColor=white) ![Google Analytics](https://img.shields.io/badge/Google_Analytics_4-E37400?style=for-the-badge&logo=googleanalytics&logoColor=white) ![Lighthouse](https://img.shields.io/badge/Lighthouse-F44B21?style=for-the-badge&logo=lighthouse&logoColor=white) ![Schema.org](https://img.shields.io/badge/Schema.org-JSON--LD-3C5A99?style=for-the-badge) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![Bing](https://img.shields.io/badge/Bing_Webmaster-258FFA?style=for-the-badge&logo=microsoftbing&logoColor=white)

> Term 1 (CPISM) · 6 sessions × 2 hours · Make websites easy to find, easy to understand and easy to use, for people and for search engines

## What you will learn

- How search engines crawl, index and rank pages, and how a results page (SERP) is built
- Use Google Search settings and advanced search operators like a researcher
- Do keyword research and write titles, meta descriptions, headings, URLs and alt text that work
- Earn backlinks the right way and connect social media with SEO (off-page SEO)
- Make sites mobile-friendly and fast (mobile-first indexing, Core Web Vitals)
- Write helpful, SEO-friendly content and grow a local business with Google Business Profile
- Add structured data (Schema.org JSON-LD), `robots.txt` and `sitemap.xml`
- Understand international SEO (`hreflang`), Social Media Optimization (SMO) and Open Graph tags
- Measure results with Google Search Console and Google Analytics 4, then run a full SEO audit

## Prerequisites

- HTML5 and CSS3 basics from [Module 02: Progressive Website Development](../02-Progressive-Website-Development/README.md)
- Responsive pages with Bootstrap from [Module 03](../03-Bootstrap-and-jQuery-for-Responsive-Web-Pages/README.md)
- Publishing a site with Git/GitHub from [Module 04](../04-Distributed-Version-Control-with-Git/README.md) (helpful for the labs, because GitHub Pages gives you a free live URL to test)

## Tools to install / sign up for

All tools below have a free plan or are fully free.

| Tool | Why you need it | Official link |
|------|-----------------|---------------|
| Google Chrome + DevTools (Lighthouse built in) | Test speed, mobile view and SEO basics | <https://www.google.com/chrome/> |
| Visual Studio Code | Edit HTML, `robots.txt`, `sitemap.xml`, JSON-LD | <https://code.visualstudio.com/> |
| Google Search Console | See how Google crawls and indexes your site | <https://search.google.com/search-console> |
| Google Analytics 4 | Measure visitors, engagement and conversions | <https://analytics.google.com/> |
| PageSpeed Insights | Core Web Vitals and speed report | <https://pagespeed.web.dev/> |
| Rich Results Test | Check structured data for Google features | <https://search.google.com/test/rich-results> |
| Schema Markup Validator | Check any Schema.org markup | <https://validator.schema.org/> |
| Bing Webmaster Tools | Index your site on Bing (and see its SEO reports) | <https://www.bing.com/webmasters> |
| Google Business Profile | Local SEO for a shop, clinic or institute | <https://www.google.com/business/> |
| Python 3.12 (optional) | Run the small SEO checker script in Session 06 | <https://www.python.org/downloads/> |

Optional third-party tools used in demos (free tiers): Ubersuggest, Semrush, Ahrefs Webmaster Tools, MozBar, Screaming Frog SEO Spider (free up to 500 URLs), GTmetrix, Yoast SEO for WordPress.

## Session index

| Session | Topic | Link |
|---------|-------|------|
| 01 | Search Engines and SEO Components, On-page and Off-page Optimization | [Open](./Session-01-Search-Engines-On-Page-and-Off-Page-SEO/README.md) |
| 02 | Practice Lab: Search Operators, Keyword Research, Meta Tags and Backlinks | [Open](./Session-02-Practice-Lab-Keywords-Meta-Tags-and-Backlinks/README.md) |
| 03 | Mobile SEO, SEO-friendly Content and Local SEO | [Open](./Session-03-Mobile-SEO-Content-and-Local-SEO/README.md) |
| 04 | Practice Lab: Mobile-friendly Page, Blog Post and Local Business Schema | [Open](./Session-04-Practice-Lab-Mobile-Content-and-Local-SEO/README.md) |
| 05 | Advanced SEO: International SEO, SMO, SEO Tools and Google Analytics | [Open](./Session-05-Advanced-SEO-International-SMO-Tools-and-Analytics/README.md) |
| 06 | Practice Lab: Full SEO Audit and 30-day SEO Strategy | [Open](./Session-06-Practice-Lab-SEO-Audit-and-Strategy/README.md) |

Each theory session (01, 03, 05) is followed by a hands-on practice lab (02, 04, 06). Do the labs on a real page: your Module 02/03 website is perfect.

## Module mini-project

**"Rank My Institute"** - take the responsive website you built in Modules 02-03 (or a simple site for a local business in Karachi) and make it search-ready:

1. Pick 1 main keyword and 4 supporting keywords per page, recorded in `keyword-research.csv`.
2. Give every page a unique `<title>` (50-60 characters), meta description (120-155 characters), one `<h1>`, clean URLs and descriptive `alt` text.
3. Add `robots.txt`, `sitemap.xml`, a canonical link and LocalBusiness (or EducationalOrganization) JSON-LD.
4. Add Open Graph tags so links look good on WhatsApp, Facebook and LinkedIn.
5. Publish on GitHub Pages, verify it in Google Search Console, submit the sitemap and add Google Analytics 4.
6. Score 90+ for SEO and Accessibility in Lighthouse (mobile), and pass the Rich Results Test.
7. Submit a 2-page audit report using the template from Session 06.

## Resources (official documentation)

- [Google Search Central: SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google Search Central: How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)
- [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google: Introduction to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Schema.org](https://schema.org/)
- [web.dev: Core Web Vitals](https://web.dev/articles/vitals)
- [Google Analytics 4 Help Center](https://support.google.com/analytics/)
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- [The Open Graph protocol](https://ogp.me/)
- [sitemaps.org protocol](https://www.sitemaps.org/protocol.html)

---

[⬅ Previous Module](../04-Distributed-Version-Control-with-Git/README.md) · [🏠 Term Home](../README.md) · [Start Session 01 ➡](./Session-01-Search-Engines-On-Page-and-Off-Page-SEO/README.md) · [Next ➡](../eProject/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
