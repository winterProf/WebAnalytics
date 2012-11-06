from twitter import *

# Secret Keys                                                                                                                       
oauth_token = "563118238-vROWGhnOwsIXM3F2kKhwiZjqdainQmfH85zE0qVD"
oauth_secret = "0wiCCMzrL6P9esfTkf6avgelAT7PHLFlUZpnaSyCl4"
CONSUMER_KEY = "uX6aVpYRbM0SxHjqIvKqQ"
CONSUMER_SECRET = "ybTOvljBWmnhG5BWqioM1crZoydTMZ0WbucNRspsus"


# Create a TwitterTools instance                                                                                                    
t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

# Get a random selection of tweets from public timeline                                                                             
someTweets = t.statuses.public_timeline()

for tweet in someTweets:
    print tweet['user']['created_at']

