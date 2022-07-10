<?php

function ips()
	{
		if (!empty($_SERVER['HTTP_CLIENT_IP']))
		{
			$ip	= $_SERVER['HTTP_CLIENT_IP'];
		}
		elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])){
			$ip	= $_SERVER['HTTP_X_FORWARDED_FOR'];
		}
		else{
			$ip	= $_SERVER['REMOTE_ADDR'];
		}
		return $ip;
	}

$ip = ips();
$host = gethostbyaddr($_SERVER['REMOTE_ADDR']);
$ipp = $_SERVER['HTTP_HOST'];
$tarayici = $_SERVER['HTTP_USER_AGENT'];
$dil = $_SERVER['HTTP_ACCEPT_LANGUAGE'];
$sikistirma = $_SERVER['HTTP_ACCEPT_ENCODING'];
$p = $_SERVER['SERVER_PROTOCOL'];
$istk = $_SERVER['REQUEST_METHOD'];
$port = $_SERVER['REMOTE_PORT'];
$sdil = $_SERVER['SERVER_SOFTWARE'];

$fp = fopen('log.txt', 'a');
fwrite($fp,"\n\n\n".'İp Adresi: '.$ip."\n\n".'Host: '.$host."\n\n".'İp Port: '.$ipp."\n\n".'User Agent: ' .$tarayici."\n\n".'Sayfa Dili: '.$dil."\n\n".'Sıkıştırma: '.$sikistirma."\n\n".'Protokol: '.$p."\n\n".'İstek: '.$istk."\n\n".'Port: '.$port."\n\n".'Server Dili: '.$sdil."\n\n\n");
fclose($fp);