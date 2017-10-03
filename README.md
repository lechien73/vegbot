# Gary the /r/vegan helper bot

Gary needs the following dependencies installed:

* urllib2
* PRAW
* google-api-python-client

Gary uses eval() to determine the correct response from the keyword. For this reason, keep the responses to the dictionary list.

Put the Reddit username and password into config_vegbot.py along with the Google API key, Custom Search Engine ID, and Reddit client ID and secret.

If Gary is down and you decide to run the bot yourself, then remove the query counter code or install the counter_update.php script on your own server and update the query code accordingly. I've redacted the actual link.

## Change log

| Date 				| Changes			|
|---				|---				|
| January 8, 2017   | Final version 1 live  				|
|   				|   				|
| February 18, 2017	| Added -pmop, -pm and -above switches	|
|   				|   				|
| March 16, 2017	| Jokes, nukes and restaurant reviews	|
|   				|   				|
| April 29, 2017	| Extra error trapping for subs where wer're banned	|
|   				|   				|
| July 20, 2017		| Version 1.2. Engine overhaul, OAuth authentication, works with PRAW 5.0.1 	|
|   				|   				|
| August 13, 2017	| Improved error trapping and improved statistics for charting 	|
|   				|   				|
| September 30, 2017	| Added thank you note for "Good bot" votes. Statistics improvements. 	|
|   				|   				|

30th September, 2017
