n = int(input("Enter Term"))
if(n<= 0):
    print("Invalide Term")
else:
    if(n == 1):
        print("0")
    elif(n == 2):
        print("0 1")
    else:
        a = 0
        b = 1
        print(a)
        print(b)
        for i in range(3,n + 1):
            c = a + b
            print(c)
            a = b
            b = c
