fname = input("enter file:")
fhand = open(fname)
unique = list()
for line in fhand:
    line = line.split()
    for word in line:
        if word not in unique:
            unique.append(word)
unique.sort()
print(unique)
