<?php
// mail-config.example.php -> copy to mail-config.php and fill in. Never commit mail-config.php!
return [
    'host'      => 'sandbox.smtp.mailtrap.io',   // or smtp.gmail.com
    'port'      => 587,
    'username'  => 'your-username',
    'password'  => 'your-app-password',
    'from'      => 'noreply@yoursite.pk',
    'from_name' => 'Aptech Student Site',
    'to'        => 'you@example.com',             // where contact messages go
];
