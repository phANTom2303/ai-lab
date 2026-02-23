from queue import Queue


def main():
    rows = int(input("Enter number of rows = "))
    cols = int(input("Enter number of columns = "))
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    
    print("Enter Matrix cells (1 for wall, 0 for empty cell)")
    for i in range(rows):
        matrix[i] = list(map(int, input().split()))
    print(matrix)
    
    source = list(map(int, input("Enter Starting cell x and y coords").split()))
    treasure = list(map(int, input("Enter Treasure Cell x and y").split()))
    
    print(source, treasure)

main()


"""
Test Case
5
5
0 0 0 1 0
0 0 1 0 0
0 1 0 0 0
0 0 1 1 0
0 0 0 0 0
0 0
0 5
"""
