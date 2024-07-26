str = 'X-DSPAM-Confidence: 0.8475'
colpos = str.find(":")
#print(colpos)
num = str[colpos+1:]
#num = float(num)
print(num)
