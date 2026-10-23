<?php
// contact.php  - first run: composer require phpmailer/phpmailer
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
require __DIR__ . '/vendor/autoload.php';
$cfg = require __DIR__ . '/mail-config.php';

$status = ''; $errors = [];
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? ''); $email = trim($_POST['email'] ?? ''); $msg = trim($_POST['message'] ?? '');
    if ($name === '') $errors[] = 'Name is required';
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'Valid email is required';
    if (mb_strlen($msg) < 10) $errors[] = 'Message must be at least 10 characters';

    if (!$errors) {
        $mail = new PHPMailer(true);
        try {
            $mail->isSMTP();
            $mail->Host = $cfg['host']; $mail->Port = $cfg['port'];
            $mail->SMTPAuth = true; $mail->Username = $cfg['username']; $mail->Password = $cfg['password'];
            $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
            $mail->CharSet = 'UTF-8';

            $mail->setFrom($cfg['from'], $cfg['from_name']);
            $mail->addAddress($cfg['to']);
            $mail->addReplyTo($email, $name);          // reply goes to the visitor

            $mail->isHTML(true);
            $mail->Subject = "New contact message from $name";
            $safe = nl2br(htmlspecialchars($msg));
            $mail->Body    = "<h3>New message</h3><p><b>Name:</b> " . htmlspecialchars($name) .
                             "<br><b>Email:</b> " . htmlspecialchars($email) . "</p><p>$safe</p>";
            $mail->AltBody = "Name: $name\nEmail: $email\n\n$msg";   // plain-text version

            if (!empty($_FILES['file']['tmp_name']) && $_FILES['file']['error'] === UPLOAD_ERR_OK
                && $_FILES['file']['size'] < 2_000_000) {
                $mail->addAttachment($_FILES['file']['tmp_name'], basename($_FILES['file']['name']));
            }
            $mail->send();
            $status = 'Thank you! Your message has been sent.';
        } catch (Exception $e) {
            $status = 'Sorry, the message could not be sent. ' . $mail->ErrorInfo;
        }
    }
}
?>
<!DOCTYPE html><html><head><title>Contact</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-4" style="max-width:560px">
<h2>Contact Us</h2>
<?php foreach ($errors as $er): ?><div class="alert alert-danger py-1"><?= $er ?></div><?php endforeach; ?>
<?php if ($status): ?><div class="alert alert-info"><?= htmlspecialchars($status) ?></div><?php endif; ?>
<form method="post" enctype="multipart/form-data">
  <input name="name" class="form-control mb-2" placeholder="Your name">
  <input name="email" class="form-control mb-2" placeholder="Your email">
  <textarea name="message" class="form-control mb-2" rows="5" placeholder="Message"></textarea>
  <input type="file" name="file" class="form-control mb-3">
  <button class="btn btn-primary">Send</button>
</form>
</body></html>
