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
