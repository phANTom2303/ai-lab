from queue import PriorityQueue

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
    print(parent)
    
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

'''