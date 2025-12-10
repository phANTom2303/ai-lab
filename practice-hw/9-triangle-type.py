a = int(input())
b = int(input())
c = int(input())
if(a + b > c and b + c > a and a + c > b):
    if(a ==b and b == c):
        print("Equilateral Triangle")
    elif(a == b or b == c or c == a):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")