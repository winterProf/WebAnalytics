import re, urllib2
from bs4 import BeautifulSoup
import mechanize

ljuser="debutante-coder"
#try:
# 	c = urllib2.urlopen(url)
# except IOError:
# 	print "Bad URL"
# else:
# 	contents = c.read()
# 	bsoup = BeautifulSoup(contents)
# 	# links = bsoup('a')
# 	# for link in links:
# 	# 	print link
# 	paras = bsoup.findAll('p')
# 	for para in paras:
# 		print para

def getFriends(br,ljnet,ljuser,depth):
	profile_url = 'http://users.livejournal.com/' + ljuser + '/profile'
	br.open(profile_url)
	if depth < 2:
		for link in br.links(url_regex="profile"):
			getFriends(br,ljnet,link.text,depth+1)
	else:
		ljnet[ljuser] = link.text



ljnetwork = {}
br = mechanize.Browser()
depth=0
getFriends(br,ljnetwork,ljuser,depth)
		
