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
