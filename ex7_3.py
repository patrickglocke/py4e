fname = input("enter file name:")
if fname == "na na boo boo":
            print("NA NA BOO BOO TO YOU - You have been punk'd")
            quit()
try:
    fhand = open(fname)
except:
    print("file cannot be opened:", fname)
    quit()
count = 0
for line in fhand:
   
        if line.startswith("Subject:"):
            count = count + 1   
print("there were", count, "subject lines in", fname)