from twitter import *
import matplotlib.pyplot as plt
import json
import re
from time import strftime,strptime

# Secret Keys
# oauth_token = "563118238-vROWGhnOwsIXM3F2kKhwiZjqdainQmfH85zE0qVD"
# oauth_secret = "0wiCCMzrL6P9esfTkf6avgelAT7PHLFlUZpnaSyCl4"
# CONSUMER_KEY = "uX6aVpYRbM0SxHjqIvKqQ"
# CONSUMER_SECRET = "ybTOvljBWmnhG5BWqioM1crZoydTMZ0WbucNRspsus"

#t = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET), api_version="1.1")
#ts = TwitterStream(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET), api_version="1.1")
#someTweets = ts.statuses.sample()

#ts = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET), api_version="1.1", domain="search.twitter.com")
ts = Twitter(domain="search.twitter.com")

# utility function for removing duplicates
def unq(seq):
   # Not order preserving
   keys = {}
   for e in seq:
       keys[e] = 1
   return keys.keys()

# Search for debate-relevant tweets
def getTweets(tags,sentiment=False,debate=False):
	# debate tags
	if debate:
		debates = "(#debates OR @crowleyCNN)"
	else:
		debates = ""

	# tag for sentiment
	if sentiment == "pos":
		smiley = " :)"
	elif sentiment == "neg":
		smiley = " :("
	else:
		smiley = ""
	
	tag_times = {}
	for tag in tags:
		tweets = ts.search(q=tag + debates + smiley,lang="en",result_type="recent",count=100)
		for tweet in tweets['results']:
			if 'text' in tweet:
				# date format: u'Tue Oct 16 20:11:05 +0000 2012'
				tweetdate = strftime("%m_%d_%H_%M",strptime(tweet['created_at'][5:25].encode('utf8'),"%d %b %Y %H:%M:%S"))[:-1]
				#tweetdate = tweet['created_at'][17:22]
				if tweetdate in tag_times:
					tag_times[tweetdate].append(tweet['text'])
				else:
					tag_times[tweetdate] = [tweet['text']]
	
	return tag_times


# GOP hashtags
GOP = ["#romney","#tcot","#gop","#romney","@mittromney","#cantafford4more","@PaulRyanVP"]
Dem = ["#obama","@barackobama","#mittmath","#teamobamabiden","@biden"]

# get Tweets
allGOP = getTweets(GOP)
allDem = getTweets(GOP)
posGOP = getTweets(GOP,"pos")
posDem = getTweets(Dem,"pos")
negGOP = getTweets(GOP,"neg")
negDem = getTweets(Dem,"neg")

# time series of all tweets
tw_T = unq(allGOP.keys() + allDem.keys() + posGOP.keys() + posDem.keys() + negGOP.keys() + negDem.keys())
tw_T.sort()
allGOP_t = [ len(allGOP[str(x)]) if x in allGOP else 0 for x in tw_T ]
allDem_t = [ len(allDem[str(x)]) if x in allDem else 0 for x in tw_T ]
posGOP_t = [ len(posGOP[str(x)]) if x in posGOP else 0 for x in tw_T ]
posDem_t = [ len(posDem[str(x)]) if x in posDem else 0 for x in tw_T ]
negGOP_t = [ len(negGOP[str(x)]) if x in negGOP else 0 for x in tw_T ]
negDem_t = [ len(negDem[str(x)]) if x in negDem else 0 for x in tw_T ]

#debate-only Tweets
debGOP = getTweets(GOP,False,True)
debDem = getTweets(GOP,False,True)
posdebGOP = getTweets(GOP,"pos",True)
posdebDem = getTweets(Dem,"pos",True)
negdebGOP = getTweets(GOP,"neg",True)
negdebDem = getTweets(Dem,"neg",True)

# time series of debate tweets
twdeb_T = unq(debGOP.keys() + debDem.keys() + posdebGOP.keys() + posdebDem.keys() + negdebGOP.keys() + negdebDem.keys())
twdeb_T.sort()
debGOP_t = [ len(debGOP[str(x)]) if x in debGOP else 0 for x in twdeb_T ]
debDem_t = [ len(debDem[str(x)]) if x in debDem else 0 for x in twdeb_T ]
posdebGOP_t = [ len(posdebGOP[str(x)]) if x in posdebGOP else 0 for x in twdeb_T ]
posdebDem_t = [ len(posdebDem[str(x)]) if x in posdebDem else 0 for x in twdeb_T ]
negdebGOP_t = [ len(negdebGOP[str(x)]) if x in negdebGOP else 0 for x in twdeb_T ]
negdebDem_t = [ len(negdebDem[str(x)]) if x in negdebDem else 0 for x in twdeb_T ]


plt.subplots_adjust(wspace=0.5)
plt.subplot(211)
plt.plot(range(len(tw_T)),allGOP_t,'r:',allDem_t,'b:',posGOP_t,'r-+',posDem_t,'b-+',negGOP_t,'r-.x',negDem_t,'b-.x')

plt.subplot(212)
plt.plot(range(len(twdeb_T)),debGOP_t,'r:',debDem_t,'b:',posdebGOP_t,'r-+',posdebDem_t,'b-+',negdebGOP_t,'r-.x',negdebDem_t,'b-.x')
plt.show()


