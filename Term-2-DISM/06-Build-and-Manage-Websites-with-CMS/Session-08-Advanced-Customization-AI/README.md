# Session 08: Advanced Customization, AI Tools and Final Project

> Module: Build and Manage Websites with CMS · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Use AI assistants responsibly to draft content and SEO metadata
- Add a chatbot to a WordPress site
- Create custom post types and taxonomies (plugin and code)
- Debug with WP_DEBUG and fix common errors
- Plan a safe update strategy and present a final project

## 📖 Concepts Explained

### 1. AI in WordPress

AI tools (ChatGPT, Gemini, built-in AI features of SEO plugins) can **draft** blog outlines, product descriptions, SEO titles and meta descriptions, alt text and FAQ sections.

Use them responsibly:
- Always **edit and fact-check** — AI can be wrong or generic.
- Add your own experience and local details (Google rewards helpful, original content).
- Never paste private customer data into AI tools.
- Disclose AI assistance where your institute or client requires it.

Example prompt: *"Write 5 SEO titles under 60 characters and 3 meta descriptions under 155 characters for a page about weekend PHP classes in North Nazimabad, Karachi. Friendly tone."*

### 2. Chatbots

Plugins such as **Tidio** or other live-chat/chatbot widgets add a chat bubble: FAQs, lead capture, WhatsApp hand-off. Configure greeting, opening hours and auto-replies; test on mobile.

### 3. Custom Post Types (CPT) and taxonomies

Posts and pages are built-in post types. A **CPT** adds a new content type such as *Portfolio*, *Testimonials* or *Courses*, with its own menu item, archive and fields. A **custom taxonomy** groups them (e.g. *Project Type*). Create them with the **CPT UI** plugin or with code (`register_post_type`, `register_taxonomy`).

### 4. Debugging

| Problem | Typical fix |
|---|---|
| White screen / "critical error" | enable `WP_DEBUG_LOG`, read `wp-content/debug.log`; rename the last plugin's folder in `wp-content/plugins` |
| 500 Internal Server Error | regenerate `.htaccess` (Settings → Permalinks → Save), raise PHP memory limit |
| 404 on all posts | re-save permalinks |
| Plugin conflict | deactivate all plugins, re-enable one by one; switch to a default theme |
| Error establishing DB connection | check `wp-config.php` credentials and that MySQL is running |

Use **Recovery Mode** (link emailed to the admin) to log in after a fatal error.

### 5. Update strategy

Backup → update on staging → test key pages and forms → update live during low traffic → monitor.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Custom post type and taxonomy in a plugin (`courses-cpt/courses-cpt.php`)

```php
<?php
/**
 * Plugin Name: Courses CPT
 * Description: Registers a "Course" post type and a "Level" taxonomy.
 * Version:     1.0.0
 */

if ( ! defined( 'ABSPATH' ) ) exit;

add_action( 'init', function () {
    register_post_type( 'course', [
        'labels'       => [
            'name'          => 'Courses',
            'singular_name' => 'Course',
            'add_new_item'  => 'Add New Course',
        ],
        'public'       => true,
        'has_archive'  => true,                       // /courses/ archive page
        'rewrite'      => [ 'slug' => 'courses' ],
        'menu_icon'    => 'dashicons-welcome-learn-more',
        'supports'     => [ 'title', 'editor', 'thumbnail', 'excerpt' ],
        'show_in_rest' => true,                       // enables the block editor
    ] );

    register_taxonomy( 'level', 'course', [
        'labels'       => [ 'name' => 'Levels', 'singular_name' => 'Level' ],
        'hierarchical' => true,                       // behaves like categories
        'public'       => true,
        'rewrite'      => [ 'slug' => 'level' ],
        'show_in_rest' => true,
    ] );
} );

// Flush rewrite rules once on activation so /courses/ works immediately
register_activation_hook( __FILE__, function () {
    do_action( 'init' );
    flush_rewrite_rules();
} );
```

**How it works:**

After activation a **Courses** menu appears with a **Levels** taxonomy; `has_archive` creates `/courses/`. Placing the CPT in a plugin (not the theme) keeps your content type if you change themes.

### Example 2: Final project checklist (`final-project-checklist.md`)

```markdown
# Final WordPress Project – Submission Checklist

## Pages and content
- [ ] Homepage with hero, services/courses, testimonials and call to action
- [ ] About, Services/Courses, Blog and Contact pages in the main menu
- [ ] Blog: at least 3 posts, 2 categories, tags, featured images
- [ ] Portfolio or Courses section built with a Custom Post Type

## Features
- [ ] Contact form tested + embedded Google map
- [ ] Chatbot or live chat widget
- [ ] Gallery with optimised images and alt text

## Quality
- [ ] SEO plugin configured; titles and meta descriptions on every page; sitemap submitted
- [ ] Google Analytics connected
- [ ] Caching enabled; PageSpeed mobile score recorded
- [ ] Responsive on 375 px, 768 px and desktop
- [ ] Security plugin, limited logins, DISALLOW_FILE_EDIT
- [ ] Backup downloaded and restore tested

## Presentation (5–7 minutes)
- [ ] Client/purpose, site walkthrough, one technical challenge and how you solved it
```

**How it works:**

Use this list to self-check before your presentation.

## 🧪 Lab Practice

1. Use an AI assistant to draft an article outline and meta tags; then rewrite them in your own words and fact-check.
2. Install a chatbot plugin (e.g. Tidio) and set up three FAQ auto-replies.
3. Create a Portfolio CPT with CPT UI, then the Courses CPT with the code plugin; add three items each.
4. Enable `WP_DEBUG_LOG`, cause an error with a broken snippet in the child theme, read `debug.log` and fix it.
5. Write your site's update plan (who, when, how to roll back).

## 📝 Assignment

**Final project**: build and present a complete WordPress site for a real or fictional client including homepage, blog, contact page with form and map, a custom post type section (portfolio/courses/testimonials), chatbot, SEO + Google Analytics, caching, security hardening and a backup. Submit the site export, screenshots and the completed checklist.

## ❓ Quick Quiz

1. Which function registers a custom post type?
   - a) add_post_type
   - b) register_post_type
   - c) create_cpt
   - d) new_post_type
2. What does `has_archive => true` provide?
3. First step when a site shows a critical error?
4. Why put a CPT in a plugin rather than the theme?
5. Name one rule for using AI-written content.

<details>
<summary>Show answers</summary>

1. b) register_post_type
2. An archive page listing all items (e.g. /courses/).
3. Enable debug logging / check debug.log and deactivate the latest plugin.
4. So the content type survives theme changes.
5. Edit and fact-check it; add original insight; protect private data.

</details>

## 💼 Interview Questions

1. **How do you troubleshoot a plugin conflict?**

   <details><summary>Model answer</summary>

   Back up, deactivate all plugins and switch to a default theme, then re-enable one at a time until the problem returns; check debug.log and browser console.

   </details>

2. **What is a custom taxonomy?**

   <details><summary>Model answer</summary>

   A custom way to group posts or CPT items, either hierarchical like categories or flat like tags.

   </details>

3. **How can AI help a WordPress site owner, and what are the risks?**

   <details><summary>Model answer</summary>

   It speeds up drafting content, SEO metadata and chat support; risks include inaccuracies, generic content, copyright/privacy issues and over-reliance.

   </details>

## ✅ Summary

- AI drafts content and metadata; humans edit and verify.
- Chatbots add instant support and lead capture.
- CPTs and taxonomies model custom content like portfolios and courses.
- WP_DEBUG and systematic checks fix common errors; update with a plan.

---

[⬅ Previous](../Session-07-Analytics-Performance-Security/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../../07-A-Millennials-Guide-to-Entrepreneurship/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
