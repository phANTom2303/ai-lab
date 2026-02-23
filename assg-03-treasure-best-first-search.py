from queue import PriorityQueue

def isValidCell(x, y, rows, cols):
    if(x >= 0 and y >= 0 and x < rows and y < cols):
        return True
    return False 

def manhattanDistance(cell, treasure):
    return abs((cell[0] - treasure[0]) + (cell[1] - treasure[1]))

def bestFirstSearch(matrix, source, treasure, visited, parent):
    openCells = PriorityQueue()
    openCells.put((0, source))
    dirx = [0, 0, -1, 1]
    diry = [1, -1, 0, 0]
    rows = len(matrix)
    cols = len(matrix[0])
    visited[0][0] = 1
    #For each cell in priority queue, pick the best heuristic one.
    while not openCells.empty():
        dist, cell = openCells.get()
        #Process each neighbour of that cell
        for i in range(len(dirx)):
            newcellx = cell[0] + dirx[i]
            newcelly = cell[1] + diry[i]
            #check cell validity, if cell is a path, if cell has already not been opened
            if(isValidCell(newcellx, newcelly, rows, cols) and matrix[newcellx][newcelly] == 0 and  visited[newcellx][newcelly] == 0):
                visited[newcellx][newcelly] = 1 #mark as visited
                parent[newcellx][newcelly] = cell #set parent path
                md = manhattanDistance(cell, treasure) #find manhattan distance
                openCells.put((md, [newcellx, newcelly])) #put in pq
                if([newcellx, newcelly] == treasure):
                    return
                
            
def getPath(source, treasure, parent):
    current = treasure
    finalPathCells = []
    while current != source:
        finalPathCells.append(current)
        current = parent[current[0]][current[1]]
    finalPathCells.append(source)
    return finalPathCells



def display2d(matrix):
    print()
    for row in matrix:
        print(row)

def visualize_matplotlib(renderedMatrix):
    import matplotlib.pyplot as plt
    from matplotlib import colors
    import numpy as np

    rows = len(renderedMatrix)
    cols = len(renderedMatrix[0])

    # Create a numeric grid for visualization
    # 0 = Empty, 1 = Wall, 2 = Explored, 3 = Path, 4 = Start, 5 = Treasure
    display_grid = np.zeros((rows, cols))

    # Map the characters to the numeric values
    for i in range(rows):
        for j in range(cols):
            char = renderedMatrix[i][j]
            if char == '#':
                display_grid[i][j] = 1 # Wall
            elif char == '*':
                display_grid[i][j] = 3 # Path
            elif char == 'S':
                display_grid[i][j] = 4 # Start
            elif char == 'T':
                display_grid[i][j] = 5 # Treasure
            elif char == 'x':
                display_grid[i][j] = 2 # Explored
            else:
                display_grid[i][j] = 0 # Empty

    # Define colors: [Empty, Wall, Explored, Path, Start, Treasure]
    # Colors: White, Black, DeepSkyBlue, Yellow, Green, Red
    cmap = colors.ListedColormap(['white', 'black', 'deepskyblue', 'gold', 'green', 'red'])
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots(figsize=(8, 8))
    # Set window title
    fig.canvas.manager.set_window_title("Assignment 3 : Best First Search")
    
    ax.imshow(display_grid, cmap=cmap, norm=norm)
    
    # Draw grid lines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.5)
    ax.set_xticks(np.arange(-.5, cols, 1))
    ax.set_yticks(np.arange(-.5, rows, 1))
    # Hide axis labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    # Add Legend
    legend_elements = [
        plt.Rectangle((0,0),1,1, color='green', label='Start (S)'),
        plt.Rectangle((0,0),1,1, color='red', label='Treasure (T)'),
        plt.Rectangle((0,0),1,1, color='gold', label='Path (*)'),
        plt.Rectangle((0,0),1,1, color='deepskyblue', label='Explored (x)'),
        plt.Rectangle((0,0),1,1, color='black', label='Wall (#)'),
        plt.Rectangle((0,0),1,1, color='white', label='Empty (.)')
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.3, 1))

    plt.title("Best First Search with Manhattan Distance as heuristic")
    plt.tight_layout()
    plt.show()

def main():
    rows = int(input("Enter number of rows = "))
    cols = int(input("Enter number of columns = "))
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    
    print("Enter Matrix cells (1 for wall, 0 for empty cell)")
    for i in range(rows):
        matrix[i] = list(map(int, input().split()))
    
    source = list(map(int, input("Enter Starting cell x and y coords").split()))
    treasure = list(map(int, input("Enter Treasure Cell x and y coords").split()))
    
    visited = [[0 for i in range(cols)] for j in range(rows)]
    parent = [[[] for i in range(cols)] for j in range(rows)]
    parent[source[0]][source[1]] = source
    bestFirstSearch(matrix, source, treasure, visited, parent)
    finalPathCells = getPath(source, treasure, parent)
    
    #do visualization : 
    renderedMatrix = [['' for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if(matrix[i][j] == 1):
                renderedMatrix[i][j] = '#'
            else:
                if(visited[i][j] == 1):
                    renderedMatrix[i][j] = 'x'
                else:
                    renderedMatrix[i][j] = '.'
                    
    for cell in finalPathCells:
        renderedMatrix[cell[0]][cell[1]] = '*'
    
    renderedMatrix[source[0]][source[1]] = 'S'
    renderedMatrix[treasure[0]][treasure[1]] = 'T'
    print()
    for i in range(rows):
        for j in range(cols):
            print(renderedMatrix[i][j], end=' ')
        print()
        
    visualize_matplotlib(renderedMatrix)
                    

    
    
    

main()


"""
Test Case
6
10
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 0 0
0 0
0 9

Test Case 2 (Large Maze):
15
15
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 0 1 1 1 1 1 1 0
0 1 0 0 0 0 0 0 0 0 0 0 0 1 0
0 1 0 1 1 1 1 1 1 1 0 1 0 1 0
0 1 0 1 0 0 0 0 0 1 0 1 0 1 0
0 1 0 1 0 1 1 1 0 1 0 1 0 1 0
0 0 0 1 0 1 0 0 0 1 0 1 0 1 0
0 1 1 1 0 1 1 1 1 1 0 1 0 1 0
0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 0 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0
14 14
"""

"""
Time Complexity Analysis:
The Best First Search algorithm uses a Priority Queue to explore cells based on their heuristic value (Manhattan distance).
- In the worst case, we might visit every cell in the grid once.
- Let V be the number of empty cells (vertices) and E be the number of possible moves (edges). In a grid, E ≈ 4V.
- Each cell is pushed into the Priority Queue at most once.
- Priority Queue operations (insertion and extraction) take O(log V) time.
- Therefore, the worst-case Time Complexity is O(V log V) or O(R*C log(R*C)) where R is rows and C is columns.
- However, with a good heuristic, it often performs much better than BFS, though it is not guaranteed to find the shortest path.

Space Complexity Analysis:
- We store the 'visited' array of size R*C.
- We store the 'parent' array of size R*C used for path reconstruction.
- The Priority Queue can store up to O(V) cells in the worst case (e.g., if many cells are added before being processed).
- Therefore, the Space Complexity is O(V) or O(R*C).
"""
