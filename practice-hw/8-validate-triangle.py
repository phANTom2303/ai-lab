a = int(input())
b = int(input())
c = int(input())
if(a + b > c and b + c > a and a + c > b):
    print("Valid Triangle")
else:
    print("Invalid Triangle")