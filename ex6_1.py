word=input("enter string")
x = len(word)
while x > 0:
    letter = word[x-1]
    print(letter)
    x=x-1
print("done")