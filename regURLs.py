import re

regexurls = re.compile("(https?://)*([a-zA-Z0-9]+\.)*[a-zA-Z0-9]+\.[a-zA-Z]{2,4}(/[a-zA-Z0-9_\(\)\-]*)*")

fh = open("url-matching-regex-test-data.txt","r")

print "Matched:"
for line in fh:
    url = regexurls.search(line)
    if url:
        print url.group(0)

fh.close()
fh = open("url-matching-regex-test-data.txt","r")

print "Did not match:"
for line in fh:
    url = regexurls.search(line)
    if url == None and len(line)>0:
        print line


