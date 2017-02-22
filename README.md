# Gary the /r/vegan helper bot

Gary needs the following dependencies installed:

* urllib2
* PRAW
* google-api-python-client

Gary uses eval() to determine the correct response from the keyword. For this reason, keep the responses to the dictionary list.

Put the Reddit username and password into config_vegbot.py along with the Google API key and Custom Search Engine ID.

If Gary is down and you decide to run the bot yourself, then remove the query counter code or install the counter_update.php script on your own server and update the query code accordingly. I've redacted the actual link.

22nd February, 2017
