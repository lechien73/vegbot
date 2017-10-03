<?php 

$u_agent = $_SERVER['HTTP_USER_AGENT']; 

if(strlen(strstr($u_agent,"veg_bot")) == 0 ){

	$keyword = $_GET['q'];
	$subreddit = $_GET['s'];

	/* Normalise the responses for charting */

	if($keyword == "swallow" || $keyword == "bj") $keyword = "semen"; 
	if($keyword == "eskimos") $keyword = "inuit";
	if($keyword == "discord" || $keyword == "irc") $keyword = "chat";
	if($keyword == "books") $keyword = "reading";
	if($keyword == "beginners" || $keyword == "newbie") $keyword = "beginner";
	if($keyword == "america") $keyword = "usa";
	if($keyword == "britain" || $keyword == "england" || $keyword == "scotland" || $keyword == "wales"  || $keyword == "ni")
		$keyword = "uk";
	if($keyword == "eire") $keyword = "ireland";
	if($keyword == "holland") $keyword = "netherlands";

	$fname = "counter.log";
	
	$newcontent = "\n1,".$keyword.",".date("Y-m-d,H:i").",".$subreddit;
	
	$fhandle = fopen($fname,"a");
	fwrite($fhandle,$newcontent);
	fclose($fhandle);

}

?>