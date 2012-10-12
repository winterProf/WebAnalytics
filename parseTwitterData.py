from twitter import *
import pprint
import mechanize
import urllib
import re
import json
import time
# create a pretty printer
pp = pprint.PrettyPrinter(indent=3)

# Secret Keys
oauth_token = "563118238-vROWGhnOwsIXM3F2kKhwiZjqdainQmfH85zE0qVD"
oauth_secret = "0wiCCMzrL6P9esfTkf6avgelAT7PHLFlUZpnaSyCl4"
CONSUMER_KEY = "uX6aVpYRbM0SxHjqIvKqQ"
CONSUMER_SECRET = "ybTOvljBWmnhG5BWqioM1crZoydTMZ0WbucNRspsus"

# Number of random tweets to pull
NUMTWEETS = 200

# Create a TwitterTools instance
t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET), api_version="1.1")
ts = TwitterStream(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET), api_version="1.1")

# Get a random selection of tweets from public timeline
someTweets = ts.statuses.sample()
#pp.pprint(someTweets[0])

first = True
tweets = []
urls = []
location_str = []
friends = []
followers = []
regexurls = re.compile("(https?://)*([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+\.[a-zA-Z]{2,4}(/[a-zA-Z0-9_\(\)\-]*)*")

for i in range(0, NUMTWEETS):
    try:
        tweet = someTweets.next()
    except TwitterHTTPError:
        continue
    else:
        if first:
            pp.pprint(tweet)
            first = False
        tweets.extend(tweet['text'])
        urls.extend(regexurls.findall(tweet['text']))
        location_str.append(tweet['user']['location'])
        friends.append(tweet['user']['friends_count'])
        followers.append(tweet['user']['followers_count'])

br = mechanize.Browser()
br.set_handle_robots(False)
for locstr in location_str:
    #ascii_locstr = "".join((c if ord(c) < 128 else '' for c in locstr))
    ascii_locstr = re.sub("[^a-zA-Z0-9_ \,\.\-]","",locstr)
    print urllib.quote_plus(ascii_locstr)
    time.sleep(1)
    response = br.open("http://maps.googleapis.com/maps/api/geocode/json?address=" + urllib.quote_plus(ascii_locstr) + "&sensor=false")
    location_json = response.read()
    try:
        location = json.loads(location_json)
    except:
        print "Error: " + location_json
    else:
        if len(location['results']) > 0:
            print "\t" + location['results'][0]['formatted_address']
            print "\t" + str(location['results'][0]['geometry']['location']['lat']) + "," + str(location['results'][0]['geometry']['location']['lng'])

