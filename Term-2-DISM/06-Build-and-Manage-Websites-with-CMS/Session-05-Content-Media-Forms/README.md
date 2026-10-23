# Session 05: Creating and Managing Content, Media and Forms

> Module: Build and Manage Websites with CMS · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Distinguish pages from posts
- Create pages (About, Services, Contact) and blog posts with categories and tags
- Manage the Media Library and create galleries
- Embed YouTube videos, maps and iframes
- Build a contact form and use page templates and menus

## 📖 Concepts Explained

### 1. Pages vs posts

| Pages | Posts |
|---|---|
| timeless content: About, Contact, Services | time-based articles/news |
| hierarchical (parent/child) | organised by **categories** and **tags** |
| not in the blog feed or RSS | appear in blog feed, archives, RSS |

**Categories** = broad, hierarchical groups (Tutorials, News). **Tags** = specific keywords (php, laravel). Keep a small set of categories.

### 2. Block editor basics

Paragraph, Heading, Image, Gallery, Columns, Buttons, Cover, Embed, Group blocks. Type `/` to insert a block. **Patterns** are ready-made groups of blocks; **reusable (synced) patterns** update everywhere.

### 3. Media

Upload images (compress first — ideally < 200 KB, WebP), always fill **Alt text** for accessibility and SEO. Galleries: Gallery block → choose images → columns, crop, link.

### 4. Embeds

Paste a YouTube URL on its own line — WordPress embeds it automatically (oEmbed). For Google Maps use **Share → Embed a map** and paste the iframe into a **Custom HTML** block.

### 5. Forms

WPForms Lite or Contact Form 7: create the form, copy its shortcode/block onto the Contact page, test that emails arrive (use an SMTP plugin such as WP Mail SMTP on live sites).

### 6. Menus and templates

Create a navigation menu (Site Editor → Navigation, or Appearance → Menus). Choose a page **template** (e.g. "Page No Title", "Full width") in the page settings sidebar, or create new ones in the Site Editor.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Responsive map embed for a Custom HTML block (`map-embed.html`)

```html
<!-- Paste into a Custom HTML block on the Contact page -->
<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:12px">
  <iframe
    src="https://www.google.com/maps?q=North+Nazimabad+Karachi&output=embed"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0"
    loading="lazy" referrerpolicy="no-referrer-when-downgrade"
    title="Our location on Google Maps"></iframe>
</div>
```

**How it works:**

The wrapper keeps a 16:9 ratio on all screen sizes; `loading="lazy"` delays loading the map until it is visible.

## 🧪 Lab Practice

1. Create pages: Home, About, Services, Contact, Blog; set Home as the static front page and Blog as the posts page.
2. Create 2 categories and 3 posts with featured images, tags and excerpts.
3. Build a Gallery of 6 compressed images with alt text.
4. Embed a YouTube video in one post and a Google map on the Contact page.
5. Create a contact form (name, email, phone, message), place it on Contact and test a submission.

## 📝 Assignment

Complete a **Contact page** (form + map + address + WhatsApp link) and a **Blog** section with at least 3 posts in 2 categories, each with featured image, alt text, tags and an embedded video in one post. Add all pages to the main menu.

## ❓ Quick Quiz

1. Which is better for an 'About Us' page?
   - a) Post
   - b) Page
2. Categories vs tags?
3. How do you embed a YouTube video?
4. Why fill alt text?
5. Which block lets you paste an iframe?

<details>
<summary>Show answers</summary>

1. b) Page
2. Categories are broad and hierarchical; tags are specific keywords.
3. Paste the URL on its own line or use the YouTube/Embed block.
4. Accessibility for screen readers and image SEO.
5. Custom HTML block

</details>

## 💼 Interview Questions

1. **How would you structure a small business website in WordPress?**

   <details><summary>Model answer</summary>

   Static pages (Home, About, Services, Contact) in a main menu, a blog using posts and categories, forms on Contact, and consistent templates.

   </details>

2. **What is oEmbed?**

   <details><summary>Model answer</summary>

   A standard that lets WordPress turn a URL from supported sites (YouTube, X, Vimeo) into an embedded player automatically.

   </details>

3. **How do you keep media from slowing the site?**

   <details><summary>Model answer</summary>

   Resize and compress images, use WebP, lazy-load, and avoid uploading huge originals.

   </details>

## ✅ Summary

- Pages = static content; posts = dated articles with categories/tags.
- The block editor, patterns and templates build layouts fast.
- Optimise media and always write alt text.
- Embed videos/maps and add forms for interaction.

---

[⬅ Previous](../Session-04-Plugins-and-Widgets/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-06-SEO-Responsive-Caching/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
