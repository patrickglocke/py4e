n=0
y=0
z=0
while True:
    x = input("enter a number:")
    if x == "done":
        break
    else:
        try:
            x = float(x)
            n=n+1
            y=y+x
            z=y/n
        except:
            print("invalid input")
       
print(int(y),n,z)
