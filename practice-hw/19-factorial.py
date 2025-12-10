a = int(input())
if(a <= 2):
    print(a)
else:
    fact = 1
    while a > 1:
        fact *= a
        a-=1
    print(fact)