<?php
// Important parts of wp-config.php (not the whole file)

// ** Database settings ** //
define( 'DB_NAME', 'wp_mysite' );
define( 'DB_USER', 'wp_user' );
define( 'DB_PASSWORD', 'Use-A-Strong-Password-Here' );
define( 'DB_HOST', 'localhost' );
define( 'DB_CHARSET', 'utf8mb4' );
define( 'DB_COLLATE', '' );

// Unique keys and salts: generate at https://api.wordpress.org/secret-key/1.1/salt/
define( 'AUTH_KEY',  'paste-unique-phrase-here' );
// ... (7 more keys and salts)

// Table prefix: changing the default makes automated attacks a little harder
$table_prefix = 'ms24_';

// Development helpers (turn OFF on a live site)
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );       // writes to wp-content/debug.log
define( 'WP_DEBUG_DISPLAY', false );

// Hardening
define( 'DISALLOW_FILE_EDIT', true ); // removes the theme/plugin code editor from the dashboard
define( 'WP_POST_REVISIONS', 10 );    // keep at most 10 revisions per post

/* That's all, stop editing! */
if ( ! defined( 'ABSPATH' ) ) {
    define( 'ABSPATH', __DIR__ . '/' );
}
require_once ABSPATH . 'wp-settings.php';
