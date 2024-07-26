

def count(word, letter):
    global letcount
    for let in word:
        if let == letter:
            letcount = letcount + 1

letcount = 0
string = input("enter string: ")
char = input("enter char: ")
count(string, char)
print(letcount)
