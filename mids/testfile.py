fname = input("Give me the file Name:")
with open(fname) as f:
    c = f.readlines()
    print("Number of lines", len(c))
    f.seek(0)
    c = f.read().split()
    c = set(c)
    print("No of Unique words", len(c))
