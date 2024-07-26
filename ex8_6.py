num = list()
while True:
    x = input("enter number: ")
    if x == "done":
        break
    try:
        x = int(x)
        num.append(x)
    except:
        print("enter a number")
        continue
print(num)
print("max:", max(num))
print("min:", min(num))