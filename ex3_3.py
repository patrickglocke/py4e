try:
    score = float(input("enter score"))
except:
    print("enter number between 0 and 1")
    quit()
if score >1 or score <0:
    print("enter a number between 0 and 1")
    quit()
elif score >=0.9: print("A")
elif score >=0.8: print("B")
elif score >=0.7: print("C")
elif score >=0.6: print("D")
else: print("F")