a = int(input())
if(a < 0):
    a *= -1
if(a >= 0 and a <= 9):
    print("Single Digit")
elif(a >= 10 and a <= 99):
    print("2 Digits")
else:
    print("3 (or more) digits")