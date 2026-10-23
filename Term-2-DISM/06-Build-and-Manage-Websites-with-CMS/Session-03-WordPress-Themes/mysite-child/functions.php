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
