<?php
/**
 * Plugin Name: Aptech Notice Bar
 * Description: Shows a dismissible announcement bar and provides the [today] shortcode.
 * Version:     1.0.0
 * Author:      Your Name
 * License:     GPL-2.0-or-later
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // block direct access
}

// 1) Announcement bar at the top of every page
add_action( 'wp_body_open', function () {
    $text = esc_html__( 'Admissions open for the new batch — visit the Contact page!', 'aptech-notice' );
    echo '<div id="aptech-notice" style="background:#0d6efd;color:#fff;text-align:center;padding:8px">'
        . $text
        . ' <button onclick="this.parentElement.remove()" style="margin-left:10px">×</button></div>';
} );

// 2) Shortcode: [today] prints the current date in the site's timezone
add_shortcode( 'today', function () {
    return esc_html( wp_date( get_option( 'date_format' ) ) );
} );
