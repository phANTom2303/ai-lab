a = int(input())
digs = 0
while a > 0:
    digs+=1
    a//=10
print(digs)