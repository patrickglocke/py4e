fname = input("enter file name:")
fhand = open(fname)
count = 0
num = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        #print(line)
        colpos = line.find(":")
        #print(colpos)
        num = float(line[colpos+1:].strip())+num
        count = count+1
print("avg:", num/count)