'''
Using the tweepy package, build a script that classifies a twitter handle
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import tweepy, pprint

consumer_key = "OuqXzzx8yQdlxOxJ93wHrUH55"
consumer_secret = "YVZKkxfIfCoBYWftZuiB3nHKX03HBsvwgK5MimBK2MCTcsIAud"
access_token = "65966796-eiZyWKQBi9IBtlbo6WF69YYhgUM1fkonQbnEnqYcl"
access_secret = "jxamZSqxkETMSGpFVAzqZX1Xziwhsuiw5W0bk3yqytxvR"
# handle = "bliiir"

class User():

    """Create a user object

    Attributes:
        api (OBJ):                  Tweepy connection
        follower_handles (STR):     The twitter handles of the users followers
        followers (LIST):           A list of the users followers
        group (STR):                The category I put the user in - possible values are High, Medium, Low
        handle (STR):               The users own handle (screen_name)
        num_followers (INT):        Number of users that follows me
        num_following (INT):        Number of users I follow
    """

    def __init__(self, api, handle):
        self.api = api
        self.handle = handle

    # Followers and friends
    def entourage(self):
        self.num_following = len(api.friends_ids(self.handle))
        self.num_followers = len(api.followers_ids(self.handle))

    # Categori I put people in
    def group(self):
        if self.num_followers > 1000:
            self.group = "high"
        elif self.num_followers > 100:
            self.group = "medium"
        else:
            self.group = "low"
        return(self.group)

    # Standard output from print
    def __str__(self):
        self.entourage()
        stats = f"handle: {self.handle:10s} followers: {self.num_followers:10d} following: {self.num_following:10d} group: {self.group().rjust(14)}"
        return stats

    # Get a list of the users followers
    def get_followers(self):
        self.followers = api.followers()
        return self.followers

    # Create a list of handles for the users' followers for a recursive instantiation loop
    def get_follower_handles(self):
        self.follower_handles = []
        followers = self.get_followers()
        for follower in followers:
            self.follower_handles.append(follower._json['screen_name'])
        return(self.follower_handles)



############    SETUP BEGIN     ############

# Connect to tweepy and get an api connection object back
def connect():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return(api)

# Get connected
api = connect()

# Extract my own handle
my_handle = api.me()._json['screen_name']

# Make a User object for myself
myself = User(api, my_handle)

# Print myself
print(myself)

############    SETUP END       ############


# Enough about me - lets talk about you!!

# Get list of follower handles
follower_handles = myself.get_follower_handles()

# Instantiate a new user for each follower handle
followers = []
for each in follower_handles:
    print(each)
    usr = User(api, each)
    followers.append(usr)

for follower in followers:
    print(follower)











#### DUMP

###

# * Create a user class (see attributes below)
# * Get a list of handles for users I am following
# * Add the users to a dictionary
# * Search for @mentions of those users
# * Add the number of @mentions for each user to the dictionary

# I will sort by followers in three categories according to the number of followers:

# 2: inf      > high      > 1000
# 1: 1000     > medium    > 100
# 0: 100      > low       > 0


    # self.num_followers = api.me()._json['followers_count']
    # self.num_following = api.me()._json['friends_count']



    # def timeline(self):
    #     self.timeline = api.home_timeline()
    #     return self.timeline

    # def tweets(self):
    #     tl = []
    #     for tweet in timeline():
    #         tl.append(tweet)
    #     self.tweets = None

    # def ratio(self):
    #     pass

