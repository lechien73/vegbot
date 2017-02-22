<?php 

$u_agent = $_SERVER['HTTP_USER_AGENT']; 

if(strlen(strstr($u_agent,"veg_bot")) > 0 ){

	$fname = "counter.log";
	$fhandle = fopen($fname,"r");
	$content = fread($fhandle,filesize($fname));

	$newcontent = intval($content) + 1;

	$fhandle = fopen($fname,"w");
	fwrite($fhandle,$newcontent);
	fclose($fhandle);

}

?>