from queue import Queue

def isValid(x,y, rows, cols):
    if(x >= 0 and x < rows and y >= 0 and y < cols):
        return True
    return False

def bfs(matrix, path, start, finish):
    rows = len(matrix)
    cols = len(matrix[0])    
    visited = [[0 for i in range(cols)] for j in range(rows)]
    
    q = Queue()
    q.put(start)
    visited[start[0]][start[1]] = 1
    dirs = [[1,0],[0,1], [-1,0],[0,-1]]
    while(not q.empty()):
        node = q.get()
        if(node == finish):
            break
        
        x = node[0]
        y = node[1]
        for eachDir in dirs:
            nx = x + eachDir[0]
            ny = y + eachDir[1]
            if(isValid(nx, ny, rows, cols) and visited[nx][ny] == 0 and matrix[nx][ny] == 0):
                path[nx][ny] = [x,y]
                visited[nx][ny] = 1
                q.put([nx,ny])

dirs = [[1,0],[0,1], [-1,0],[0,-1]]
def dfs(matrix, path, visited, x, y, finish ):
    if([x,y] == finish):
        return
    for eachDir in dirs:
        nx = x + eachDir[0]
        ny = y + eachDir[1]
        if(isValid(nx, ny, rows, cols) and visited[nx][ny] == 0 and matrix[nx][ny] == 0):
            path[nx][ny] = [x,y]
            visited[nx][ny] = 1
            nodes += 1 + dfs(matrix, path, visited, nx, ny, finish)
            
    
def visualize(matrix, path):
    visualzer = matrix
    node = finish
    while node != [-1,-1]:
        visualzer[node[0]][node[1]] = "P"
        node = path[node[0]][node[1]] 
    
    for row in visualzer:
        for cell in row:
            if(cell == 0):
                print(".", end=" ")
            elif(cell == 1):
                print("W", end=" ")
            else:
                print(cell, end=" ")
        print()
        

rows = int(input("Enter number of rows = "))
cols = int(input("Enter number of columns = "))
matrix = [[0 for i in range(cols)] for j in range(rows)]

path = []
for i  in range(rows):
    temp = []
    for j in range(cols):
        temp.append([-1,-1])
    path.append(temp)

print("Path : ")
for row in path:
    print(row)

print("Enter the maze :")
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input())
        
sx = int(input("Enter start x :"))
sy = int(input("Enter start y :"))
start = [sx, sy]

fx = int(input("Enter finish x :"))
fy = int(input("Enter finish y :"))
finish = [fx, fy]

print("\nEntered Maze : ")
for row in matrix:
    for cell in row:
        if(cell == 0):
            print(".", end="")
        else:
            print("W", end="")
        print(" ",end="")
    print()
    
print("Start = ",start)
print("Finish = ", finish)

# BFS Call : 
print("\nResult using DFS : ")
bfs(matrix, path, start, finish)

if(path[finish[0]] == -1):
    print("No Possible Path")
else:
    visualize(matrix, path)

# DFS Call :  
rows = len(matrix)
cols = len(matrix[0])
    
visited = [[0 for i in range(cols)] for j in range(rows)]

path = []
for i  in range(rows):
    temp = []
    for j in range(cols):
        temp.append([-1,-1])
    path.append(temp)

dfs(matrix, path, visited, sx, sy, finish)

print("\nResult using DFS : ")
if(path[finish[0]] == -1):
    print("No Possible Path")
else:
    visualize(matrix, path)
