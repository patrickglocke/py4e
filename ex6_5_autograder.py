text = "X-DSPAM-Confidence:    0.8475"

colpos = text.find(":")
#print(colpos)

num = text[colpos+1:] #take everything AFTER colon, remove whitespace
print(num)

num = float(num) #float convert
print(num) #print
