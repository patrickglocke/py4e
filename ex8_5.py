fname = input("enter file:")
fhand = open(fname)
count =0
for line in fhand:
    line = line.split()
    if len(line) == 0 or len(line) <3 or line[0] != 'From':
        continue
    print(line[1])
    count = count +1
print(count)