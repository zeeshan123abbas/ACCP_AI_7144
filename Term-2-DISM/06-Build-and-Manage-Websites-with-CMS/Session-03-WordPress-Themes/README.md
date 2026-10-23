# Session 03: Exploring WordPress Themes

> Module: Build and Manage Websites with CMS · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Explain what a theme does and how it is structured
- Install and activate themes from the directory or a .zip
- Customise a site with the Customizer or the Site Editor
- Edit layouts with the Block Editor and patterns
- Create a child theme and add custom CSS
- Describe page builders such as Elementor

## 📖 Concepts Explained

### 1. What a theme controls

A **theme** controls how content looks: layout, colours, fonts, headers, footers and templates. Content stays in the database, so you can switch themes without losing posts.

| Theme type | Customise with | Examples |
|---|---|---|
| **Block theme** (modern) | Site Editor (Appearance → Editor), `theme.json` | Twenty Twenty-Four, Twenty Twenty-Five |
| Classic theme | Customizer (Appearance → Customize), widgets | Astra, GeneratePress, OceanWP |

### 2. Template hierarchy (classic themes)

WordPress picks the most specific template available: e.g. for a single post `single-post.php` → `single.php` → `singular.php` → `index.php`. Minimum theme = `style.css` + `index.php`.

### 3. Installing themes

- **Appearance → Themes → Add New** → search → Install → Activate.
- **Upload Theme** → choose `.zip` (premium themes).
- Always preview with **Live Preview** first.

### 4. Child themes

Never edit a theme directly — updates overwrite your changes. A **child theme** inherits everything from the parent and only contains your changes.

### 5. Page builders

Elementor, Beaver Builder and Divi offer drag-and-drop design. They are quick for beginners but add page weight; the native block editor with patterns is lighter. Elementor's free version is enough for this module.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Child theme stylesheet (`mysite-child/style.css`)

```css
/*
 Theme Name:   MySite Child
 Template:     twentytwentyfour
 Description:  Child theme for my practice site
 Version:      1.0.0
 Text Domain:  mysite-child
*/

/* Your custom styles */
:root {
  --brand: #0d6efd;
}
.wp-block-button__link {
  border-radius: 999px;
  background: var(--brand);
}
.site-footer, footer.wp-block-template-part {
  border-top: 3px solid var(--brand);
}
```

**How it works:**

`Template:` must be the parent theme's **folder name**. Upload the folder to `wp-content/themes/` and activate it.

### Example 2: Child theme functions (`mysite-child/functions.php`)

```php
<?php
// mysite-child/functions.php
add_action( 'wp_enqueue_scripts', function () {
    // Load the child stylesheet after the parent's
    wp_enqueue_style(
        'mysite-child-style',
        get_stylesheet_uri(),
        [],
        wp_get_theme()->get( 'Version' )
    );
} );

// Add a custom footer note to every page (classic hook; works in block themes too)
add_action( 'wp_footer', function () {
    echo '<p style="text-align:center;font-size:12px">Built during the Aptech CMS module</p>';
} );
```

**How it works:**

Block themes load the parent's styles automatically; we enqueue our own `style.css`. `wp_footer` is an **action hook** that lets us add output without editing templates.

## 🧪 Lab Practice

1. Install two themes (one block theme, one classic like Astra) and switch between them; note what changes and what stays.
2. Using the Site Editor, change the header (logo, site title, navigation) and global colours/typography.
3. Build a homepage with block patterns: hero, services, testimonials, call-to-action.
4. Create and activate the `mysite-child` theme (zip the folder and upload it).
5. Install Elementor, design one landing page and compare its loading speed with a block-editor page.

## 📝 Assignment

Design a homepage for a fictional coaching centre using a theme of your choice: header with logo and menu, hero section, three course cards, testimonials and footer. Submit screenshots and a short note on what you customised and why.

## ❓ Quick Quiz

1. What is the minimum set of files for a classic theme?
   - a) header.php + footer.php
   - b) style.css + index.php
   - c) functions.php only
   - d) theme.json only
2. Why use a child theme?
3. Where do you customise a block theme?
4. Which line in style.css links a child to its parent?
5. Name one drawback of page builders.

<details>
<summary>Show answers</summary>

1. b) style.css + index.php
2. So parent theme updates do not overwrite your changes.
3. Appearance → Editor (Site Editor).
4. `Template: parent-folder-name`
5. Heavier pages / lock-in to the builder.

</details>

## 💼 Interview Questions

1. **Explain the WordPress template hierarchy.**

   <details><summary>Model answer</summary>

   WordPress looks for the most specific template file for the requested content and falls back step by step to index.php.

   </details>

2. **What are hooks (actions and filters)?**

   <details><summary>Model answer</summary>

   Points where themes/plugins can run code (actions) or modify data (filters) without changing core files.

   </details>

3. **Block themes vs classic themes?**

   <details><summary>Model answer</summary>

   Block themes are built from HTML block templates and theme.json and edited in the Site Editor; classic themes use PHP templates and the Customizer.

   </details>

## ✅ Summary

- Themes control presentation; content lives in the database.
- Install from the directory or upload a .zip; preview first.
- Customise via Site Editor (block) or Customizer (classic).
- Put code changes in a child theme.

---

[⬅ Previous](../Session-02-Setting-Up-WordPress/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-04-Plugins-and-Widgets/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
