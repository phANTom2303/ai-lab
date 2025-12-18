v = int(input("Enter number of vertices = "))
e = int(input("Enter number of edges = "))
matrix = [[0 for i in range(v)] for j in range(v)]

print("Enter each edge (src, dest, wt) format :")
for i in range(e):
    src = int(input())
    dest = int(input())
    wt = int(input())
    matrix[src][dest] = wt
        
print(matrix)