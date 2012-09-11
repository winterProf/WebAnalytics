from twitter import *
import pprint
# create a pretty printer
pp = pprint.PrettyPrinter(indent=3)

# Secret Keys
oauth_token = ""
oauth_secret = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

# Create a TwitterTools instance
t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

# Get a random selection of tweets from public timeline
someTweets = t.statuses.public_timeline()
pp.pprint(someTweets[0])

for tweet in someTweets:
    print tweet['text']



