def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if(n2 != 0):
        return n1/n2

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
c = input("Enter : \n 'A' for add\n'S' for Subtract\n'M' for multiply\n'D' for division\nYour Choice : ")

if(c == 'A' or c == 'a'):
    print(add(n1, n2))
elif(c == 'S' or c == 's'):
    print(sub(n1, n2))
elif(c == 'M' or c == 'm'):
    print(mul(n1, n2))
elif(c == 'D' or c == 'd'):
    print(div(n1, n2))
else:
    print("Incorrect choice")
    
