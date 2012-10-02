import re


match_string = "(^| )[a-zA-Z0-9_\+\. ]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}( |\.|$)"

print match_string

emails = re.compile(match_string)

fh = open("testEmails.txt")

print "Match"
for line in fh:
    isphone = emails.search(line)
    if isphone:
        print line,

fh.close()
fh = open("testEmails.txt")

print "\n\n"
print "No match"
for line in fh:
    isphone = emails.search(line)
    if isphone == None:
        print line,
