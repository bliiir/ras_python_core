'''
Using the tweepy package, build a script that classifies a twitter handle
into different groups according to the number of their followers.

* Create a twitter user class - handle, followers, mentions, following, tweets
* Get a list of handles for users I am following
* Add the users to a dictionary
* Search for @mentions of those users
* Add the number of @mentions for each user to the dictionary

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import tweepy
# import numpy

import pprint
#pp = pprint.PrettyPrinter(indent=4)

consumer_key = "OuqXzzx8yQdlxOxJ93wHrUH55"
consumer_secret = "YVZKkxfIfCoBYWftZuiB3nHKX03HBsvwgK5MimBK2MCTcsIAud"

access_token = "65966796-eiZyWKQBi9IBtlbo6WF69YYhgUM1fkonQbnEnqYcl"
access_token_secret = "jxamZSqxkETMSGpFVAzqZX1Xziwhsuiw5W0bk3yqytxvR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

t = api.get_user("bliiir")
f = api.followers("bliiir")
for each in  f:
    pprint.pprint(each)
