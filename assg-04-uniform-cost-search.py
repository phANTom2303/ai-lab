from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(adjList, path):
    G = nx.DiGraph()
    
    # Add edges to the graph
    for u, neighbors in enumerate(adjList):
        for v, weight in neighbors:
            G.add_edge(u, v, weight=weight)
            
    # Use shell layout for less clutter, or increase k in spring_layout
    pos = nx.spring_layout(G, k=0.5, iterations=50) # Increased spacing
    # Alternative: pos = nx.shell_layout(G)
    
    plt.figure("Assg 04 : Uniform Cost Search", figsize=(10, 8)) # Increased figure size

    
    # Draw non-path nodes and edges
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
    nx.draw_networkx_labels(G, pos)

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Highlight path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='lightgreen', node_size=500)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2, arrows=True)
        
    plt.title("Uniform Cost Search Path")
    plt.axis('off')
    plt.show()

def uniformCostSearch(adjList, source):
    totalNodes = len(adjList)
    distances = [10000000 for i in range(totalNodes + 1)]
    parent = [-1 for i in range(totalNodes + 1)]
    parent[source] = source
    
    allNodes = PriorityQueue()
    allNodes.put((0, source))
    while(allNodes.qsize() > 0):
        dist, node = allNodes.get()
        if(dist > distances[node]):
            continue
        
        for padosi in adjList[node]:
            padosiNode = padosi[0]
            padosiDist = padosi[1]
            
            if(dist + padosiDist < distances[padosiNode]):
                newDistance = dist + padosiDist
                distances[padosiNode] = newDistance
                parent[padosiNode] = node
                allNodes.put((newDistance, padosiNode))
    return parent
                
        
    
def main():
    nodes = int(input("\nEnter number of cities(nodes) : "))
    edges = int(input("\nEnter number of roads(edges) : "))

    adjList = [[] for i in range(nodes + 1)]
    print("\nEnter edges in the format : city1 city2, weight :\n")
    for e in range(edges):
        c1, c2 , w= map(int, input().split())
        adjList[c1].append([c2, w])

    nodenum = 0
    for row in adjList:
        print(nodenum, end=" -> ")
        for edge in row:
            print(edge, end=" ")
        nodenum += 1
        print()

    source = int(input("Enter Source City : "))
    destination = int(input("Enter Destination City : "))
    parent = uniformCostSearch(adjList, source)
    path = []
    current = destination
    while(current != source):
        path.append(current)
        current = parent[current]
    path.append(source)
    path.reverse()
    print(path)
    visualize_graph(adjList, path)
    
main()
'''
Sample Test Case:

Input:
5
6
0 1 2
0 3 5
1 2 4
3 1 5
3 4 2
2 4 1
0
4

Large Test Case:
10
18
0 1 4
0 2 2
1 2 5
1 3 10
2 4 3
4 3 4
4 5 2
3 5 1
2 6 8
5 6 3
3 7 6
5 7 5
6 8 6
7 8 4
6 9 7
7 9 2
8 9 3
0 4 15
0
9
'''