fname = input("enter file name:")#file name
x=0
y=0
fhand=open(fname)#open file
for str in fhand: #loop through all text in file
    if str.startswith("X-DSPAM-Confidence:"):
        colpos = "X-DSPAM-Confidence:".find(":")#look for string
        num = float(str[colpos+1:])
        x=x+num
        y=y+1#pick the number out
    #add the numbers up
#print(colpos)
#print(num)
#print(x)
#print(y)
print("Average spam confidence:", x/y)#count the numer of numbers
    #print average