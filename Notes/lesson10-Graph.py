#Notes ------------------------------------------------------------------------
'''
Graphs
    Non-Linear data structure consisting of a Vertices (nodes) and edges (connection between nodes [lines])
    A tree is a type of graph (very special one not typical at all)

    Types of Graphs:
        - Directed Graph -> edges has directions
        - Undirected -> edges have no directions
        - Weighted -> edges have weight (distance, cost, time, etc)
        - Unweighted -> Edges do not have weights
    
    Ways to represent graphs:
        - Adjacency Matrix -> 2D array which shows if there is an edge connecting the verticies (1) if not
                              then 0
        - Adjacency List -> It is an array of multiple lists, each list corresponds to a node and the content
                            of it contains the adjecent nodes (the ones that are connected to it)
        - Edge List -> A list of all the edges in the graph (all the lines that connect the nodes)

    Graph Operations:
        - Adding a vertex (a node)
        - Adding an Edge (a line connecting 2 nodes)
        - Traversal:
            + DFS
            + BFS
    
    Applications of Graph Data Structures:
        Dijkstra's algorigm:
            Used to find the shortest path from the start vertex to the end vertex
            Used in google maps and networking routes 
            ONLY USED WHEN WEIGHT IS ALL POSITIVE
            Heap Sort is used for this algo to work
                - using min heap 
                - it will check the vertex's neighbours and the weights between them
                - it will then extract the min value between the weights and use that edge to move 
                - To avoid reprocessing it will use a set that keeps track of all vertices that we visited

        Prim's algorithm:
            Minimum spaning tree
            All the node must be connected with the lowest weight total (shortest path) AND must not have a cycle

                



'''
#IM LATE WITH CODE FUUUUCK ----------------------------------------------------
'''
#Graph DS Operations ---------------
class graph:
    def __init__(self):
        self.graph = {}                         #Creates the graph (constructor) into a dictionary 

    def addVertex(self,vertex):                 #Adds the Vertex
        if vertex not in self.graph:            #if the vertex is no in the graph it will add it to the graph
            self.graph[vertex] = []             #adds the vertex as the key and anything inside is its values/adjecent to
    
    def addEdge(self, vertex1, vertex2, directed = False):
        if vertex1 not in self.graph:           #if the vertex does not exist it will call the addVertex func
            self.addVertex(vertex1)
        if vertex2 not in self.graph:
            self.addVertex(vertex2)

        self.graph[vertex1].append(vertex2)     #adds the vertex2 to the list of vertex1 to show that they are connected
        if not directed:
            self.graph[vertex2].append(vertex1) #same thing if not directed but other way around
    
    def __str__(self):
        return str(self.graph)

#dfs trav -------   
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()                         #creates a set so it can have no duplicates
    visited.add(start)                          #adds the start value to the set (can not be added again cuz no dups)
    print(start, end = " ")

    for neighbor in graph[start]:               #for every neighbor (connected vertex) it will check if not in the set
        if neighbor not in visited:
            dfs(graph, neighbor,visited)        #if not in set it will call the function again using the neighbor as the start 
                                                #this will keep going until all the vertices are added to the set

#bfs trav -------
from collections import deque

def bfs(graph, start):
    visited = set()                             #Creates a set called visited
    visited.add(start)                          #adds the start value to the set
    queue = deque([start])                      #adds the start value to the queue
    while queue:                                
        vertex = queue.popleft()                #vertex 
        print(vertex, end = " ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def hasCycle(graph, vertex, visited, parent):   #Checks if there is a cycle
    visited.add(vertex)                         #addes the veertex to the set of visited
    for neighbour in graph[vertex]:             #for every neighbour of the specific vertex/node
        if neighbour not in visited:            #it will check if it is not in visited and - if not - recall the func to do it again
            if hasCycle(graph, vertex, visited, parent):
                return True                     #if the func is true it will return true
            elif parent != neighbour:           #if the func is false but the parent is not a neighbour then it will return true
                return True
        return False                            #if neither requirments are met  it will return false
    
def containsCycle(graph):
    visited = set()                             #Creates a set called Visited
    for vertex in graph:                        #for every node in the graph
        if vertex not in visited:               #if the vertex/node is not in the visited it will call the hasCycle func
            if hasCycle(graph,vertex,visited,None):
                return True                     #if the func returns true then there is a cycle and it returns true    
        return False                            #If the func is not true it will return false and that means there is no cycle
    
def shortestPath(graph, start, goal):
    visited = set()                             #creats a set called visited
    queue = deque([(start, [start])])           #creates a queue
    while queue:                                #while the queue is active 
        (vertex, path) = queue.popleft()        #it addes the vertex
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if neighbour == goal:
                    return path + [neighbour]
                else:
                    visited.add(neighbour)
                    queue.append((neighbour, path + [neighbour]))
    return None


g = graph()

g.addEdge('A','B')
g.addEdge('A','C')
g.addEdge('B','D')
g.addEdge('C','D')
g.addEdge('D','E')

print("Graph: ", g)
print(" ---DFS Trav--- ")
dfs(g.graph,'A')
print()
print(" ---BFS Trav--- ")
bfs(g.graph,'A')

print("Does this graph contains a cycle? ", containsCycle(g.graph))
print("")
'''

#Weighted Graphs -------------------
class graph:
    def __init__(self):
        self.graph = {}                         #creates a dictionary            

    def addEdge(self, u, v, weight):            #creates an edge by connecting 2 nodes (u and v) and giving a weight 
        if u not in self.graph:                 #if u not in the graph then it makes a list under the u key
            self.graph[u]= []
        if v not in self.graph:                 #if v not in the graph then it makes a list under the v key
            self.graph[v] = []
        self.graph[u].append((v, weight))       #append 2 values under the u key and they are the node v and the weight between them
        self.graph[v].append((u, weight))       #appends 2 values under the v key and they are the node u and the weight between them
    
    def printGraph(self):                       #prints out the graph in a specific way
        for node in self.graph:                 #for each node in the graph it will print 
            print(f"{node} -> {self.graph[node]}")

#Prim's Algo ----------------
    def prims(self, start):
        mst = []
        visited = set()
        minHeap = [(0,start,None)]

        while minHeap:
            weight, currentVer, fromVer = heapq.heappop(minHeap)

            if currentVer in visited:
                continue
            visited.add(currentVer)

            if fromVer is not None:
                mst.append((fromVer,currentVer,weight))
            for neighbour, edgeWeight in self.graph[currentVer]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (edgeWeight, neighbour, currentVer))
        return mst


#Dijkstra Algo --------------
import heapq 

def dijkstra(graph,start):
    queue = []                                                  #Creates a queue list
    heapq.heappush(queue,(0,start))                             
    distances = {vertex: float('inf') for vertex in graph}      #creates a dictionary with a vertex key for each vertex in the graph with a float value inside  
    distances[start] = 0                                        #gives the key start a value of 0
    visited = set()                                             #creates a set called visited

    while queue:                                                #while the queue is true
        currentDis, currentVer = heapq.heappop(queue)           #added the current distance and the vertex to the queue
        if currentVer in visited:                               #if the current vertex is in visted then continue 
            continue
        visited.add(currentVer)                                 #if not in visited then add the vertex to visited

        for neighbour, weight in graph[currentVer]:             #for each neightbour and weight in key currentVer
            distance = currentDis + weight                      #distance is calculated as the current distance + the weight of the new edge
            if distance < distances[neighbour]:                 #if the distance calculated is less then the distance already calculated 
                distances[neighbour] = distance                 #then it will be the new distance
                heapq.heappush(queue, (distance,neighbour))     
    return distances                                            #returns the distances dictionary

'''
#Dijkstra Example -----------
g = graph()
g.addEdge('A','B',6)
g.addEdge('A','C',2)
g.addEdge('B','D',8)
g.addEdge('C','D',5)
g.addEdge('D','E',10)
g.addEdge('D','F',15)
g.addEdge('E','G',2)
g.addEdge('F','G',6)

g.printGraph()

print(dijkstra(g.graph, 'A'))
'''

#Prim Example ---------------
g = graph()
g.addEdge('A','B',4)
g.addEdge('A','H',8)
g.addEdge('B','C',8)
g.addEdge('B','H',11)
g.addEdge('C','I',2)
g.addEdge('C','F',4)
g.addEdge('C','D',7)
g.addEdge('D','F',14)
g.addEdge('D','E',7)
g.addEdge('E','F',10)
g.addEdge('F','G',2)
g.addEdge('G','H',1)
g.addEdge('G','I',6)
g.addEdge('H','I',7)

g.printGraph()

mst = g.prims('A')
print("\n ---Minimum Spanning Tree--- ")
for edge in mst:
    print(f"{edge[0]}-{edge[1]} (weight {edge[2]})")
