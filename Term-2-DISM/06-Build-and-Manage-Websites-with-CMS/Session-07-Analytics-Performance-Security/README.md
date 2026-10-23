# Session 07: Analytics, Performance and Security

> Module: Build and Manage Websites with CMS · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Connect Google Analytics 4 with Site Kit or a tracking snippet
- Measure speed with PageSpeed Insights and GTmetrix
- Harden WordPress: security plugin, login limits, file-editing off
- Configure automatic updates
- Create, download and restore backups

## 📖 Concepts Explained

### 1. Analytics

**Google Analytics 4 (GA4)** shows visitors, sources (Google, social, direct), popular pages, devices and conversions (form submissions).

Two ways to connect:
1. **Site Kit by Google** plugin: sign in with Google, it connects Analytics and Search Console and shows stats in the dashboard.
2. Manually add the GA4 `gtag.js` snippet to the `<head>` (child theme `functions.php` or a header-code plugin).

### 2. Speed testing

| Tool | Shows |
|---|---|
| PageSpeed Insights | Core Web Vitals (lab + real user data) |
| GTmetrix | waterfall of every file, page size, request count |
| Browser DevTools → Lighthouse | local audit |

### 3. Security essentials

| Risk | Defence |
|---|---|
| Brute-force logins | strong passwords, limit login attempts, 2FA, no "admin" username |
| Outdated plugins/themes | auto-updates, remove unused ones |
| Malware | Wordfence/Solid Security scan, only official downloads |
| Code editing if hacked | `DISALLOW_FILE_EDIT` |
| Data loss | automatic off-site backups |
| Eavesdropping | HTTPS (SSL certificate) |

### 4. Updates

Dashboard → Updates. Enable auto-updates for minor core releases, trusted plugins and themes. Before big updates: back up, test on a **staging** copy.

### 5. Backups

**UpdraftPlus**: schedule database + files backups to Google Drive/Dropbox; restore in one click. **All-in-One WP Migration**: export the whole site into one file — great for moving from localhost to live hosting.

Rule **3-2-1**: 3 copies, 2 different media, 1 off-site.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Adding GA4 manually via the child theme (`ga4-snippet.php`)

```php
<?php
// Add to your child theme's functions.php. Replace G-XXXXXXXXXX with your Measurement ID.
add_action( 'wp_head', function () {
    if ( is_user_logged_in() ) {
        return; // do not count your own admin visits
    }
    $id = 'G-XXXXXXXXXX';
    ?>
    <script async src="https://www.googletagmanager.com/gtag/js?id=<?php echo esc_attr( $id ); ?>"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', '<?php echo esc_js( $id ); ?>');
    </script>
    <?php
}, 5 );
```

**How it works:**

The `wp_head` hook prints the tracking code inside `<head>`; logged-in users are skipped so your own testing does not distort statistics.

### Example 2: WordPress security checklist (`security-checklist.md`)

```markdown
# Security checklist

- [ ] Admin username is not "admin"; all admins use strong unique passwords
- [ ] Two-factor authentication enabled for administrators
- [ ] Login attempts limited (security plugin)
- [ ] Wordfence / Solid Security installed, scan run, issues fixed
- [ ] `DISALLOW_FILE_EDIT` set in wp-config.php
- [ ] WP_DEBUG off on the live site
- [ ] Unused themes and plugins deleted
- [ ] Auto-updates on for core minor releases and trusted plugins
- [ ] HTTPS active and forced
- [ ] Daily/weekly backups to an off-site location; one restore tested
- [ ] Database table prefix not `wp_` (new sites)
- [ ] User roles reviewed (lowest role needed)
```

**How it works:**

Work through the list for your project site and keep it with your documentation.

## 🧪 Lab Practice

1. Install Site Kit and connect GA4 (or add the snippet with your own Measurement ID).
2. Visit your site from a phone and see the visit in GA4 Realtime.
3. Run GTmetrix and PageSpeed; note page size and number of requests.
4. Install Wordfence, run a scan, enable login attempt limits and 2FA.
5. Create a full backup with UpdraftPlus (or All-in-One WP Migration), download it, and restore it on a fresh local install.

## 📝 Assignment

Produce a **site health report**: GA4 screenshot, speed scores, security scan results, list of hardening steps applied, backup schedule and proof of a successful restore.

## ❓ Quick Quiz

1. Which Google plugin connects Analytics and Search Console?
   - a) Jetpack
   - b) Site Kit
   - c) Rank Math
   - d) Akismet
2. What does limiting login attempts prevent?
3. Name a WordPress backup plugin.
4. What is the 3-2-1 backup rule?
5. Why test updates on staging first?

<details>
<summary>Show answers</summary>

1. b) Site Kit
2. Brute-force password guessing.
3. UpdraftPlus (or All-in-One WP Migration).
4. 3 copies, 2 media types, 1 off-site.
5. To catch conflicts or breakage before they affect the live site.

</details>

## 💼 Interview Questions

1. **How would you secure a new WordPress site?**

   <details><summary>Model answer</summary>

   Strong credentials and 2FA, limited logins, security plugin, updates, minimal plugins, DISALLOW_FILE_EDIT, HTTPS, least-privilege roles and regular off-site backups.

   </details>

2. **What metrics in GA4 matter for a small business?**

   <details><summary>Model answer</summary>

   Users, traffic sources, top pages, engagement rate and key events such as form submissions or WhatsApp clicks.

   </details>

3. **How do you migrate a site from localhost to live hosting?**

   <details><summary>Model answer</summary>

   Use a migration plugin export/import, or copy files plus a database dump and update URLs (search-replace), then fix permalinks.

   </details>

## ✅ Summary

- GA4 + Site Kit measure visitors and conversions.
- PageSpeed and GTmetrix diagnose performance.
- Harden logins, update regularly and remove unused code.
- Automate off-site backups and test restores.

---

[⬅ Previous](../Session-06-SEO-Responsive-Caching/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-08-Advanced-Customization-AI/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
