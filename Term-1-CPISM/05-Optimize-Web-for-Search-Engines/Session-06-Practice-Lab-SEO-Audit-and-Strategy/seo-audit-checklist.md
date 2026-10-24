# SEO Audit Checklist

Website: ______________________  Auditor: ______________  Date: ____________

Mark each item: ✅ OK · ❌ Problem · ➖ Not applicable. Write problems into `audit-report-template.md`.

## A. Technical SEO
| # | Check | How to test | Result |
|---|-------|-------------|--------|
| A1 | Site loads on HTTPS and http redirects to https | Type `http://` version in browser | |
| A2 | Only one version is used (www or non-www) | Try both; one should redirect | |
| A3 | `robots.txt` exists and does not block important pages | Open `/robots.txt` | |
| A4 | `sitemap.xml` exists, lists only live pages, submitted | Open `/sitemap.xml`; Search Console → Sitemaps | |
| A5 | Important pages are indexed | Search Console → Pages; URL Inspection | |
| A6 | No important page has `noindex` by mistake | View source / crawler | |
| A7 | No broken internal links (404) | Screaming Frog → Response Codes | |
| A8 | No redirect chains (A→B→C) | Crawler → Redirects | |
| A9 | Mobile-friendly (viewport, no sideways scroll, readable text) | DevTools device mode, Lighthouse | |
| A10 | Core Web Vitals: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 | PageSpeed Insights | |
| A11 | Clean URLs (lowercase, hyphens, no long parameters) | Browse the site | |
| A12 | Canonical tags point to the right URL | View source / crawler | |
| A13 | Custom, helpful 404 page | Visit `/this-page-does-not-exist` | |

## B. On-page SEO
| # | Check | Result |
|---|-------|--------|
| B1 | Every page has a unique title (30-60 chars, keyword near start) | |
| B2 | Every page has a unique meta description (120-155 chars) | |
| B3 | Exactly one `<h1>` per page; headings in logical order | |
| B4 | Each page targets one main keyword that matches search intent | |
| B5 | Content is helpful, original and not thin (no copied text) | |
| B6 | Images have descriptive `alt`, are compressed and sized | |
| B7 | Internal links use descriptive anchor text; key pages within ~3 clicks | |
| B8 | Author, date and contact details visible (trust / E-E-A-T) | |
| B9 | Structured data present and valid (Organization, LocalBusiness, Article, Breadcrumb) | |
| B10 | Open Graph tags for social sharing | |
| B11 | `<html lang>` set; `hreflang` correct if multiple languages | |

## C. Off-page SEO
| # | Check | Result |
|---|-------|--------|
| C1 | Number of referring domains recorded (baseline) | |
| C2 | No obvious spam / paid links without `rel="sponsored"` | |
| C3 | Brand mentions without links found (link opportunities) | |
| C4 | Active, consistent social profiles linking to the site | |

## D. Local SEO (if a local business)
| # | Check | Result |
|---|-------|--------|
| D1 | Google Business Profile claimed, verified and complete | |
| D2 | NAP identical on website, GBP, Facebook, directories | |
| D3 | Reviews: count, average rating, owner replies | |
| D4 | LocalBusiness JSON-LD on contact/home page | |
| D5 | Bing Places / Apple Business Connect listing | |

## E. Analytics and tracking
| # | Check | Result |
|---|-------|--------|
| E1 | Search Console verified (and Bing Webmaster Tools) | |
| E2 | GA4 installed on every page | |
| E3 | Key events set (form submit, WhatsApp/phone click) | |
| E4 | GA4 linked with Search Console | |
| E5 | KPI baseline recorded (impressions, clicks, CTR, organic sessions) | |

**Totals:** ✅ ___ ❌ ___ ➖ ___
