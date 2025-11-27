rows = int(input("Enter number of rows = "))
cols = int(input("Enter number of columns = "))
matrix = [[0 for i in range(cols)] for j in range(rows)]

print("Enter each Element of the matrix :")
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input())
        

print(matrix)