def chop(t):
    del t[0]
    del t[-1]

def middle(t):
    return t[1:-1]

letters = ["a", "b", "c", "d"]
mid = middle(letters)
print(mid)
chop(letters)
print(letters)
x = mid is letters
print(x)
y=chop(letters)
print(y)