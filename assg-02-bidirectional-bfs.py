from queue import Queue

def expandLevel(nodeQueue, adjList, ancestor, visited, visitedFlag):
    oppositeFlag = visitedFlag * (-1)
    size = nodeQueue.qsize()
    for i in range(size):
        node = nodeQueue.get()
        for padosi in adjList[node]:
              # For each padosi, 3 cases : unvisited, visited by this traversal, visited by opposite traversal
            if(visited[padosi] == 0):# unvisited
                visited[padosi] = visitedFlag
                nodeQueue.put(padosi)
                ancestor[padosi] = node
            elif(visited[padosi] == oppositeFlag):#visited by opposite traversal
                commonNode = padosi
                commonNodeAncestor = node 
                return [commonNode, commonNodeAncestor, visitedFlag]
    return []

def backtrackAndBuildPath(ancestor, start, end):
    path = []
    while(start != end):
        path.append(start)
        start = ancestor[start]
    path.append(end)
    return path

def biderectionalBFS(nodes ,adjList, source, destination):
    visited = [0 for i in range(nodes + 1)]
    ancestor = [0 for i in range(nodes + 1)]

    forwardQueue = Queue()
    backwardQueue = Queue()

    forwardQueue.put(source)
    visited[source] = 1
    backwardQueue.put(destination)
    visited[destination] = -1
    commonNode = -1
    res = []
    while(True):
        # Expand 1 level from forward search
        res = expandLevel(forwardQueue, adjList, ancestor, visited, 1)
        if(len(res) > 0):
            break

        # Expand 1 level from backward search
        res = expandLevel(backwardQueue, adjList, ancestor, visited, -1)
        if(len(res) > 0):
            break
    
    direction = res[2]
    srcpath = []
    destpath = []
    # Case 1 : Common Node was found from forward search (res[2] = 1)
    if(direction == 1):
        srcpath = backtrackAndBuildPath(ancestor, res[1], source)
        destpath = backtrackAndBuildPath(ancestor, res[0], destination)
    else: # Case 2 : common node was found from backward search
        srcpath = backtrackAndBuildPath(ancestor, res[0], source)
        destpath = backtrackAndBuildPath(ancestor, res[1], destination)
        
    srcpath.reverse()
    finalpath = srcpath + destpath    
    print("Result : ")
    print(finalpath)
    


def main():
    nodes = int(input("\nEnter number of cities(nodes) : "))
    edges = int(input("\nEnter number of roads(edges) : "))

    adjList = [[] for i in range(nodes + 1)]
    print("\nEnter edges in the format : city1 city2 :\n")
    for e in range(edges):
        c1, c2 = map(int, input().split())
        adjList[c1].append(c2)
        adjList[c2].append(c1)


    nodenum = 0
    for row in adjList:
        print(nodenum, end=" -> ")
        for edge in row:
            print(edge, end=" ")
        nodenum += 1
        print()

    source = int(input("Enter Source City : "))
    destination = int(input("Enter Destination City : "))
    
    biderectionalBFS(nodes, adjList, source, destination)
    

main()


"""
Sample input : 

12
17
1 2
1 5 
1 3
2 4
3 6
4 5
5 6
4 7
5 8
6 7
7 10
8 10
8 11
7 11
10 12
8 12
11 12
1
2
"""
