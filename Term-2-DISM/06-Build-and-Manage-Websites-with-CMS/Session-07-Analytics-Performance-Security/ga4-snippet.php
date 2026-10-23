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
