h = input("Enter Hours:")
#add error check for string and <=0
try:
    h = float(h)
except:
    print("enter a numeric input")
    quit()
r = input("Enter Rate:")
#add error check for string and <=0
try:
    r = float(r)
except:
    print("enter a numeric input")
    quit()
if h > 40 :
    p = 1.5*r*(h-40)+40*r
else :
    p = r*h
print("Pay:", p)