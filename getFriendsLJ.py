from bs4 import BeautifulSoup
import mechanize

ljuser="debutante-coder"

def getFriends(br,ljnet,ljuser,depth):
	profile_url = 'http://users.livejournal.com/' + ljuser + '/profile'
	try:
		br.open(profile_url)
		br.follow_link(url_regex="profile")
	except:
		print "Could not open page for " + ljuser
		return []
	else:
		for link in br.links(url_regex="profile"):
			if link.text != "[IMG]":
				if depth < 2:
					templist = getFriends(br,ljnet,link.text,depth+1)
					ljnet.extend(templist)
				else:
					ljnet.append(ljuser + "," + link.text + "\n")
		return ljnet


ljnetwork = []
br = mechanize.Browser()
depth=0
ljnetwork.extend(getFriends(br,ljnetwork,ljuser,depth))
fh = open("friendlist.csv","w")
for line in ljnetwork:
	fh.write(line)
fh.close()
