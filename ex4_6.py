def computepay(h, r):
    try:
        h = float(h)
    except:
        print("enter a numeric input")
        quit()
    try:
        r = float(r)
    except:
        print("enter a numeric input")
        quit()
    if h > 40 :
        p = 1.5*r*(h-40)+40*r
    else :
        p = r*h
    return p

h= input("enter hours:")
r= input("enter rate:")
p= computepay(h, r)
print("Pay:", p)