from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(adjList, visited, path, title):
    G = nx.Graph()
    
    # Add nodes and edges from adjList (index-1 to match user's 1-based indexing if needed, 
    # but based on code, adjList is size nodes+1, using indices 1..nodes)
    for i in range(1, len(adjList)):
        G.add_node(i)
        for neighbor in adjList[i]:
            G.add_edge(i, neighbor)
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))
    
    # Draw all nodes first (default color)
    valid_nodes = range(1, len(adjList))
    nx.draw_networkx_nodes(G, pos, nodelist=valid_nodes, node_color='lightgray', node_size=500)
    
    # Separate nodes by category
    forward_visited = [i for i in range(1, len(visited)) if visited[i] == 1 and i not in path]
    backward_visited = [i for i in range(1, len(visited)) if visited[i] == -1 and i not in path]
    path_nodes = path
    
    # Draw forward visited nodes (e.g., green)
    nx.draw_networkx_nodes(G, pos, nodelist=forward_visited, node_color='lightgreen', label='Forward Search', node_size=500)
    
    # Draw backward visited nodes (e.g., orange)
    nx.draw_networkx_nodes(G, pos, nodelist=backward_visited, node_color='orange', label='Backward Search', node_size=500)
    
    # Draw path nodes (e.g., red)
    nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='red', label='Final Path', node_size=600)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    
    # Draw path edges specifically
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    
    # Labels
    nx.draw_networkx_labels(G, pos)
    
    plt.title(title)
    plt.legend(scatterpoints=1)
    plt.show()

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
    visualize_graph(adjList, visited, finalpath, "Bidirectional BFS")
    

def unidirectionalBFS(adjList, nodes, source, destination):
    q = Queue()
    q.put(source)
    visited = [0 for i in range(nodes + 1)]
    visited[source] = 1
    ancestor = [0 for i in range(nodes + 1)]
    ancestor[source] = source
    found = False
    while(q.qsize() > 0):
        node = q.get()
        for padosi in adjList[node]:
            if(visited[padosi] == 0):
                visited[padosi] = 1
                ancestor[padosi] = node
                q.put(padosi)
                if(padosi == destination):
                    found = True
                    break
        if(found):
            break
                    
    path = backtrackAndBuildPath(ancestor, destination, source)
    path.reverse()
    print(path)
    visualize_graph(adjList, visited, path, "Uniderectional BFS")
            
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
    unidirectionalBFS(adjList, nodes, source, destination)    

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
6 9
7 10
8 10
8 11
9 11
10 12
8 12
11 12
1
12
"""
