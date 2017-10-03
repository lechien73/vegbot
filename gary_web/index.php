<!DOCTYPE html>
<head>
    <title>Gary Bot</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <style type="text/css">
		pre {font-family: 'Courier New', monospace;}
	</style>
</head>
<body>
	<div class = "container">
	<a href="./statistics.html"><span class="glyphicon glyphicon-stats" aria-hidden="true"></span><strong> View Gary's usage statistics</strong></a>
	<h1>Gary v1.2</h1>
	<h3>General Information</h3>
	<p>I'm Gary - the <a href="www.reddit.com/r/vegan">/r/vegan</a> helper bot. I was written to make it easier to respond to some common questions about veganism so that users don't have to keep copying and pasting the same information over and over again.</p>
	<p>Updated keywords are usually pushed out at 9.00am GMT each day.</p>
	<h3>Usage within /r/vegan</h3>
	<p>You can call me from within the /r/vegan sub by replying to any comment with:</p>
	<pre>@Gary! query</pre>
	<p>Where "query" is any of the following keywords (ignore any part in brackets, they're purely explanatory):</p>
	<ul>
<li>beginner (or beginners or newbie)</li>
<li>boyfriend</li>
<li>B12</li>
<li>bible</li>
<li>books (or reading - updated 15/8/17)</li>
<li>canines</li>
<li>chat</li>
<li>cheese</li>
<li>discord</li>
<li>eggs</li>
<li>eskimos</li>
<li>ethics</li>
<li>foodchain</li>
<li>girlfriend</li>
<li>help</li>
<li>honey (updated 15/8/17)</li>
<li>inuit</li>
<li>irc</li>
<li>joke</li>
<li>labmeat</li>
<li>lions</li>
<li>maycontain</li>
<li>nukes (you cannot use this keyword in r/vegan)</li>
<li>peta</li>
<li>nutrition</li>
<li>protein</li>
<li>reading (or books - updated 15/8/17)</li>
<li>soy</li>
<li>swallow (or semen or bj - yes, the age old question)</li>
</ul>
<p>You can also ask about any of the following countries, and I'll give you videos showing how animals are treated there:</p>
<ul>
<li>america (or usa)</li>
<li>australia</li>
<li>britain (or england, scotland, wales, uk)</li>
<li>canada</li>
<li>china</li>
<li>france</li>
<li>ireland</li>
<li>italy (new 30/7/17)</li>
<li>germany</li>
<li>netherlands (or holland)</li>
<li>spain</li>
<li>sweden</li>
</ul>
<p>If you want to know what good vegan restaurants there are in a particular city, then use any of the following city names:</p>
<ul>
<li>charleston (in South Carolina)</li>
<li>dublin (Ireland)</li>
<li>jackson (Mississippi)</li>
<li>london</li>
</ul>
<p>More cities will be added as we get content for them.</p>
<p>Or you can ask for a meal idea, and I'll search some hand-picked vegan recipe sites to give you some ideas. So, try asking me about:</p>
<ul>
<li>breakfast</li>
<li>dinner</li>
<li>snacks</li>
</ul>
<p>By default, I reply to you, and tag the OP so that they get alerted to the comment. You can override this behaviour by using the "-above" option, which will force Gary to reply directly to the OP. So:</p>

<pre>@Gary! Eggs -above</pre>

<p>will send reply to the OP instead of to you. To receive your answer as a PM, use the "-pm" option. Help text is <em>always</em> sent as a PM.</p>
<p>If you use the "-pmop" switch, then I'll send the information as a private message to the OP. This is useful if you want to send someone info on a sub where Gary is banned. So:</p>

<pre>@Gary! Eggs -pmop</pre>

<p>will send the eggs information as a private message to the OP instead of as a comment reply in the sub.</p>
<p>My name can appear anywhere in the comment. You can just use the trigger word, or I'll pick it out of a sentence. So:</p>
<pre>@Gary! canines</pre>
<p>will give the same response as:</p>
<pre>Tell me about canines @Gary!</pre>
<p>Be aware, though, that if you include multiple keywords in your comment, I'll only process the first one. None of the trigger words are case sensitive, so I treat: Eggs, eggs, eGGs and EgGs as the same.</p>
<h3>Usage from another subreddit</h3>
<p>If you're in a vegan debate on another subreddit and need a bit of backup, then you can call me by my username:</p>

<pre>/u/gary_bot query</pre>

<p>You can use the same keywords as above. Certain keywords produce expanded output if they are requested from outside /r/vegan.</p>
<p>Note, though, that I'm banned from:</p>
<ul>
<li>/r/AdviceAnimals</li>
<li>/r/AskReddit</li>
<li>/r/australia</li>
<li>/r/babyelephantgifs</li>
<li>/r/CringeAnarchy</li>
<li>/r/Denmark</li>
<li>/r/facepalm</li>
<li>/r/Fitness</li>
<li>/r/NoStupidQuestions</li>
<li>/r/SubredditDrama</li>
<li>/r/The_Donald</li>
<li>/r/TumblrInAction</li>
</ul>
<p>If you still want to request information in these subreddits, then use the -pmop switch as documented above.</p>
<h3>Why Gary?</h3>
<p>We had a lot of good suggestions for names for the bot, but it was always going to be Gary. Charlotte was suggested as a potential name, after the spider from Charlotte's web who saves Wilbur from being slaughtered, but the name was too long to type to easily call the bot.</p>
<p>The name Gary comes from <a href="http://metro.co.uk/2016/09/29/vegans-have-renamed-all-of-their-cheese-gary-6160907/">one woman's rant saying that vegan cheese should be called 'Gary' instead of cheese.</a> Vegans accepted the name in good humour and it is now immortalised as the name of the /r/vegan helper bot.</p>
<h3>I have a suggestion</h3>
<p>If you have any suggestion for keywords, adjustments to the responses or information about vegan restaurants in your city, then send a PM to <a href="https://reddit.com/u/pizza_phoenix">/u/pizza_phoenix.</a></p>
<p>If you'd like to help out with cleaning up my code or adding enhancements, <a href="https://github.com/lechien73/vegbot">then here is my current code.</a> Feel free to clone my repository and create a pull request. I need extra error-trapping and could probably run more efficiently.</p>
<p><b>
<?php
$fname = "./counter.log";
$fhandle = fopen($fname,"r");
$line = fgets($fhandle);
$count = 0;
while(!feof($fhandle)) {
    $line = fgets($fhandle);
    if ($line!==FALSE) {
	    $myArray = explode(',', $line);
	    $count = $count + intval($myArray[0]);
	    $lastword = $myArray[1];
	    $lastdate = $myArray[2];
	    $lasttime = $myArray[3];
	    $lastreddit = $myArray[4];
    }
}

echo $count;
?></b>
 queries served so far. The last keyword was: <b>
 <?php echo $lastword; ?></b> on 
 <?php echo $lastdate; ?> at 
 <?php echo $lasttime; ?> in the <a href="https://reddit.com/r/<?php echo $lastreddit; ?>">r/<?php echo $lastreddit; ?> subreddit.</a></p>
<p>Document last updated: <em>3rd October, 2017. 8:08 GMT</em></p>
<p>Gary's engine last updated: <em>13th August, 2017. 17:25 GMT</em></p>
</div>
</body>
<script type="http://code.jquery.com/jquery.min.js"></script>
<script type="../bootstrap/js/bootstrap.min.js"></script>
</html>
