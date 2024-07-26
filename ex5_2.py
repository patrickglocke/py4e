largest = None
smallest = None
while True:
    x=input("enter a number:")
    if x=="done":
        break
    try:
        x=float(x)
        for y in [x]:
            if largest is None or x>largest:
                largest = x
            if smallest is None or x<smallest:
                smallest = x
        continue
    except:
        print("invalid input")
print("max is", largest)
print("min is", smallest)