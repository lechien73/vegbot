import urllib2
import praw
import os
import re
from collections import deque
from time import sleep
from config_vegbot import *
from responses import *
import json
from googleapiclient.discovery import build
from random import randint

txt_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) veg_bot',
    'Accept-Language': 'en-US',
    'Accept-Encoding': 'text/html'
}

comment_header_template = """


Hi, %s here is the information you requested for /u/%s:


"""

pmop_header = """


Hi, %s here is the information %s requested for you:


"""

help_header_template = """


Hi %s, %s


"""

not_here = """

I'm sorry, this keyword can't be used in r/vegan. If you want to send it as a PM, then use the -pm or -pmop switches.




%s

"""

livemode = True

subreddit = "vegan"

cache = deque(maxlen = 500)

r = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_secret,
                     password=reddit_password,
                     user_agent='The /r/vegan helper',
                     username=reddit_user_id)


print "Logged in"

searchWord = set(["@gary!", "@Gary!", "@GARY!"])

def findRecipe(search_term, api_key, cse_id, **kwargs):
    altlink = ""
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    if int(res['searchInformation']['totalResults']) == 0:
        resultsvar = []
    else:
        resultsvar = res['items']
    for source in resultsvar:
        altlink = altlink + "["+source['title']+"]("+source['link']+")\n\n"
    altlink = altlink + "%s\n\n"
    return altlink


def find_words(comment_body, words, stripspecial):

    if stripspecial:

        comment_body = re.sub('[-#$!@?.,:;()]', '', comment_body)
    
    comment_words = comment_body.split()

    for word in comment_words:
        if word in words:
            print word
            return word

    return "Empty"

def bot_action(comment, othersub, sendaspm):

    nopost = False
    send_pm = False
    send_op = False

    answerWhere = set(["-here", "-above", "-pm", "-pmop"])

    comment_header = comment_header_template

    if othersub:
        comment_footer = ""
        sidebar = ""
    else:
        comment_footer = comment_footer_template
        sidebar = "Always read the links in the sidebar --------->"

    parent = comment.parent()

    print parent

    wheretoanswer = find_words(comment.body.lower(), answerWhere, False)

    if wheretoanswer == "-pm":
        send_pm = True
        sidebar = ""

    if wheretoanswer == "-pmop" or sendaspm:
        send_pm = True
        send_op = True
        sidebar = ""

    trigger = find_words(comment.body.lower(), triggerWords, True)

    parentauthor = parent.author

    if debug:
        print parentauthor

    parentname = parentauthor.name

    author = comment.author
    
    requesterName = author.name

    comment_reply = ""

    if trigger == "Empty":
        nopost = True
        print "Ignoring it...no keyword found"
    elif trigger == "help":
        comment_reply = helptext
        sidebar = ""
        comment_header = help_header_template
        if not send_op:
            parentname = ""
        send_pm = True
    elif trigger == "breakfast":
        comment_reply = findRecipe("vegan breakfast", my_api_key, my_cse_id, num=5)
        sidebar = ""
    elif trigger == "dinner":
        comment_reply = findRecipe("vegan dinner", my_api_key, my_cse_id, num=5)
        sidebar = ""
    elif trigger == "snacks":
        comment_reply = findRecipe("vegan snacks", my_api_key, my_cse_id, num=5)
        sidebar = ""
    elif trigger == "nukes":
        if othersub:
            comment_reply = nukes
        else:
            comment_reply = not_here
    elif trigger == "nutrition":
        if othersub:
            comment_reply = nutrition
        else:
            comment_reply = nutritionrvegan
    elif trigger == "joke":
            sidebar = ""
            comment_reply = eval(trigger + str(randint(1,jokeNumber)))
            comment_header = "Hi, %s here is the joke you requested in /u/%s's thread:\n\n"
    else:
        comment_reply = eval(trigger)

    if livemode == True and nopost == False:

        if not send_pm:

            if wheretoanswer != "-above":
                comment.reply(comment_header % (requesterName, parentname) + comment_reply % (sidebar) + comment_footer)
            else:
                if comment.is_root:
                    parent = comment.submission

                parent.reply(comment_header % (requesterName, parentname) + comment_reply % (sidebar) + comment_footer)
                
        else:
            if not send_op:
                r.redditor(requesterName).message('Information From Gary', comment_header % (requesterName, parentname) + comment_reply % (sidebar) + comment_footer)
            else:
                r.redditor(parentname).message('Information From ' + requesterName, pmop_header % (parentname, requesterName) + comment_reply % (sidebar) + comment_footer)

    if (livemode == False and nopost == False) or debug:
            print(comment_header % (requesterName, parentname) + comment_reply + comment_footer)

    cache.append(comment.id)

    # Begin query counter code

    f = urllib2.Request(counter_url, '', txt_headers)
    response = urllib2.urlopen(f)
    print response.read()

    # End query counder code

first = True
debug = True
running = True

while running == True:

    if debug:
        print "Initial loop"

    ccount = 0

    for c in r.subreddit(subreddit).stream.comments():

        if debug:
            print "Processing stream"

        if first is True:
            cache.append(c.id)

        author = c.author
        if author == None:
            writer = None
        else:
            writer = author.name

        if c.id not in cache and writer != reddit_user_id and c.banned_by == None and writer != None:

            if debug:
                print "Trying comment " + c.id
                print ccount
                ccount = ccount + 1

            if find_words(c.body, searchWord, False) != "Empty":
                try:
                    print "We found Gary!"
                    bot_action(c, False, False)

                except KeyboardInterrupt:
                    running = False
                except praw.errors.APIException, e:
                    print "[ERROR]:", e
                    print "Sleeping for a minute. Night night!"
                    sleep(60)
                except Exception, e:
                    print "[ERROR]:", e
                    if e.lower() == "http error":
                        bot_action(c, False, True)
                        print "Sending the info as a PM because we're banned here."
                    print "There has been an error, and I'm scared!"

            for mention in r.inbox.mentions():
                if debug:
                    print "Mention loop"
                if mention.id not in cache:
            
                    if mention.new:
                        print "It's the Bat Signal!"
                        bot_action(mention, True, False)
                        mention.mark_read()

        first = False