import collections

infile = open("testfile.txt")
words = collections.Counter()

for line in infile:
    words.update(line.split())
                              
for word, count in words.iteritems():
    print (word, count)