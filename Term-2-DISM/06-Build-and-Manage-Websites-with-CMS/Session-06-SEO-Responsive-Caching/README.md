# Session 06: SEO, Mobile Responsiveness and Caching

> Module: Build and Manage Websites with CMS · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Apply on-page SEO basics
- Configure Rank Math or Yoast for titles, meta descriptions and sitemaps
- Optimise slugs, headings and image alt text
- Explain caching and install a caching plugin
- Test and fix mobile layouts and run PageSpeed Insights

## 📖 Concepts Explained

### 1. On-page SEO checklist

| Element | Good practice |
|---|---|
| Focus keyword | one main phrase per page, e.g. "php course karachi" |
| SEO title | ≤ 60 characters, keyword near the start |
| Meta description | 120–155 characters, a clear benefit + call to action |
| Slug | short, lowercase, hyphens: `/php-course-karachi/` |
| Headings | one H1 (title), logical H2/H3 |
| Content | useful, original, 600+ words for articles |
| Images | compressed, descriptive file names, alt text |
| Links | internal links to related pages, a few authoritative external links |

SEO plugins add title/meta fields, XML sitemaps (`/sitemap_index.xml`), schema markup and checklists. Submit the sitemap in **Google Search Console**.

### 2. Caching

Without caching, every visit runs PHP and database queries. A **page cache** stores the finished HTML and serves it instantly.

| Cache type | What it stores |
|---|---|
| Page cache | full HTML pages (LiteSpeed Cache, W3 Total Cache, WP Super Cache) |
| Browser cache | static files on the visitor's device |
| Object cache | database query results (Redis/Memcached) |
| CDN | copies of files on servers near visitors (Cloudflare) |

Clear the cache after design changes. Do not cache logged-in or cart/checkout pages.

### 3. Responsive design

Most Pakistani users browse on mobiles. Check every page in Chrome DevTools device mode (Ctrl+Shift+M) and the editor's mobile preview. Watch for: tiny tap targets, horizontal scrolling, huge images, unreadable font sizes. Elementor has separate desktop/tablet/mobile settings.

### 4. PageSpeed Insights

https://pagespeed.web.dev/ reports **Core Web Vitals**: LCP (largest content load, aim < 2.5 s), INP (responsiveness, < 200 ms), CLS (layout shift, < 0.1), with suggested fixes.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Per-post SEO checklist (`seo-checklist.md`)

```markdown
# SEO checklist for each post/page

- [ ] Focus keyword chosen: ______________________
- [ ] Keyword in SEO title (≤ 60 chars) and in the first paragraph
- [ ] Meta description written (120–155 chars) with a call to action
- [ ] Short slug with the keyword, no dates or stop words
- [ ] One H1; H2/H3 used in logical order
- [ ] At least 2 internal links and 1 trusted external link
- [ ] Images compressed (< 200 KB), WebP if possible, alt text describes the image
- [ ] Featured image set (used for social sharing)
- [ ] Readability: short paragraphs, bullet lists
- [ ] Checked on mobile preview
- [ ] Indexed: page is not set to noindex; sitemap submitted in Search Console
```

**How it works:**

Copy this list into your notes and tick it for every article you publish.

### Example 2: A sensible robots.txt (`robots.txt`)

```text
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://www.example.com/sitemap_index.xml
```

**How it works:**

Keeps crawlers out of the dashboard while allowing AJAX, and tells search engines where the sitemap is. SEO plugins can manage this virtually.

## 🧪 Lab Practice

1. Install Rank Math (or Yoast) with the setup wizard; set titles, separators and sitemap.
2. Fully optimise one blog post until the plugin shows a good score; record before/after.
3. Install LiteSpeed Cache (or W3 Total Cache), enable page cache, test a page in an incognito window.
4. Run PageSpeed Insights on mobile; apply three suggestions (compress images, lazy-load, minify CSS/JS) and re-test.
5. Test every page in Chrome device mode at 375 px width and fix one layout issue.

## 📝 Assignment

Write an **SEO & performance report** for your site: target keywords for 3 pages, the titles/meta descriptions you wrote, PageSpeed scores before and after optimisation (screenshots), and a list of fixes applied.

## ❓ Quick Quiz

1. Recommended maximum length of an SEO title?
   - a) 30
   - b) 60
   - c) 120
   - d) 160
2. What does a page cache store?
3. Which Core Web Vital measures layout shift?
4. Where do you submit your sitemap?
5. Should you cache the checkout page?

<details>
<summary>Show answers</summary>

1. b) About 60 characters
2. The generated HTML of pages.
3. CLS (Cumulative Layout Shift)
4. Google Search Console.
5. No.

</details>

## 💼 Interview Questions

1. **What is on-page SEO?**

   <details><summary>Model answer</summary>

   Optimising elements within your own pages — titles, meta descriptions, headings, content, images, URLs and internal links — so search engines understand and rank them.

   </details>

2. **How does caching improve WordPress performance?**

   <details><summary>Model answer</summary>

   It avoids running PHP and database queries on every request by serving stored HTML or assets, cutting server time drastically.

   </details>

3. **How do you check a site is mobile friendly?**

   <details><summary>Model answer</summary>

   Use device emulation in DevTools, real devices, the editor's responsive previews and PageSpeed Insights mobile results.

   </details>

## ✅ Summary

- Optimise titles, meta descriptions, slugs, headings, images and links.
- SEO plugins handle meta tags, sitemaps and schema.
- Caching and image optimisation make sites fast.
- Design and test mobile-first; track Core Web Vitals.

---

[⬅ Previous](../Session-05-Content-Media-Forms/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-07-Analytics-Performance-Security/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
