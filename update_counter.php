<?php 

$u_agent = $_SERVER['HTTP_USER_AGENT']; 

if(strlen(strstr($u_agent,"veg_bot")) > 0 ){

	$keyword = $_GET['q'];
	$subreddit = $_GET['s'];

	$fname = "counter.log";
	
	$newcontent = "\n1,".$keyword.",".date("Y-m-d,H:i").",".$subreddit;
	
	$fhandle = fopen($fname,"a");
	fwrite($fhandle,$newcontent);
	fclose($fhandle);

}

?>