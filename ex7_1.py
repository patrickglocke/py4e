fname = input("enter file name:")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    print(line.upper())