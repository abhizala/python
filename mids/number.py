"""
# For number of lines
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("testfile.txt"))

#For number of unique words
from collections import defaultdict
d = defaultdict(int)
for word in open('testfile.txt').read().split():
	d[word] += 1
print(d)


"""