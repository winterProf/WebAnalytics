from bs4 import BeautifulSoup
import mechanize
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys

MAX_DEPTH = 1

# utility function for getting a subset of a dictionary from a list of values
extract = lambda keys, dict: reduce(lambda x, y: x.update({y[0]:y[1]}) or x, map(None, keys, map(dict.get, keys)), {})

# utility function for transforming a dictionary edgelist to a list of tuples
def flatten(d):
	flatlist = []
	for k,v in d.iteritems():
		if isinstance(v,list):
			for v2 in v:
				flatlist.append([k,v2])
		else:
			flatlist.append([k,v])
	return flatlist


# crawling LJ for friend network
def getFriends(ljnetwork,ljuser,depth):
	br = mechanize.Browser()
	profile_url = 'http://users.livejournal.com/' + ljuser + '/profile'
	try:
		br.open(profile_url)
		br.follow_link(url_regex="profile")
	except:
		print "Could not open page for " + ljuser
		return ljnetwork
	else:
		for link in br.links(url_regex="profile"):
			if link.text != "[IMG]" and link.text != ljuser:
				if depth < MAX_DEPTH and link.text not in ljnetwork:
					ljnetwork = getFriends(ljnetwork,link.text,depth+1)
				else:
					if ljuser in ljnetwork:
						if link.text not in ljnetwork[ljuser]:
							ljnetwork[ljuser].append(link.text)
					else:
						ljnetwork[ljuser] = [link.text]
		return ljnetwork


# write edgelist to file
def writeEdgeList(ljnetwork):
	# write file with adjacency list
	fh = open("friendlist.csv","w")
	for source,targetlist in ljnetwork.iteritems():
		for target in targetlist:
			fh.write(source + "," + target + "\n")
	fh.close()

def drawNetwork(ljnetwork):
	# get the names of nodes and the list of edges
	ljnodes = ljnetwork.keys()
	ljedges = flatten(ljnetwork)

	# create a NetworkX graph from those lists
	ljnet = nx.Graph()
	ljnet.add_nodes_from(ljnodes)
	ljnet.add_edges_from(ljedges)

	# remove a-a edges (self-loops)
	ljnet.remove_edges_from(ljnet.selfloop_edges())

	# pull out k-core of graph
#	twocore = nx.k_core(ljnet,2)
#	fivecore = nx.k_core(ljnet,5)

	# get degrees of nodes
	degdist = nx.degree(ljnet)
#	degcore = nx.degree(fivecore)

	# draw network
	pos=nx.spring_layout(ljnet)
#	core_pos = extract(fivecore.nodes(),pos)
#	nx.draw_networkx_nodes(fivecore,pos,nodelist=degcore.keys(),node_color='b',node_size=20*(1.0 + np.log(degcore.values())),with_labels=True,font_color='r',font_size=18)

	nx.draw_networkx_nodes(ljnet, pos, nodelist=degdist.keys(), node_color='g',node_size=20*(1.0+np.log(degdist.values())),with_labels=True,font_color='r')

	nx.draw_networkx_edges(ljnet,pos,alpha=0.4)
	plt.show()


if __name__=="__main__":
    
    if len(sys.argv) > 1:
        ljuser=sys.argv[1]
    else:
        ljuser="debutante-coder"

    depth=0
    ljnetwork = getFriends({ljuser:[]},ljuser,depth)
    writeEdgeList(ljnetwork)
    drawNetwork(ljnetwork)
    
