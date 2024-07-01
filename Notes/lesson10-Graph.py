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
        - Adjacency Matrix -> 2D array which shows if there is an edge connecting the vertices (1) if not
                              then 0
        - Adjacency List -> It is an array of multiple lists, each list corresponds to a node and the content
                            of it contains the adjacent nodes (the ones that are connected to it)
        - Edge List -> A list of all the edges in the graph (all the lines that connect the nodes)

    Graph Operations:
        - Adding a vertex (a node)
        - Adding an Edge (a line connecting 2 nodes)
        - Traversal:
            + DFS
            + BFS
    
    Applications of Graph Data Structures:
        Dijkstra's algorithm:
            Used to find the shortest path from the start vertex to the end vertex
            Used in google maps and networking routes 
            ONLY USED WHEN WEIGHT IS ALL POSITIVE
            Heap Sort is used for this algo to work
                - using min heap 
                - it will check the vertex's neighbours and the weights between them
                - it will then extract the min value between the weights and use that edge to move 
                - To avoid reprocessing it will use a set that keeps track of all vertices that we visited

        Prim's algorithm:
            Minimum spanning tree -> uses the shortest path possible 
            All the node must be connected with the lowest weight total (shortest path) AND must not have a cycle
            Starts at a vertex and moves to the next vertex with the shortest path possible until all of the vertices are
            connected with no cycle. Backtracking is permitted so vertex C can be connected to multiple other vertices as long as
            it does not create a cycle and is allows for the lowest weight total (shortest path).
                - Used mainly in Networking
                
        Kruskal's algorithm: (will be done soon)
            Also a minimum Spanning Tree
            All nodes must be connected with the shortest path AND must not have a cycle but wat makes it different from Prim's algo
            is that it does not have a starting point. It aims to connect all of them with no backtracking while prim's backtracks.
            Prim's algo starts at a vertex while Kruskal's starts at the lightest (smallest) edge and then goes to the next one (they do
            not have to be connected) it goes in ascending order until all vertices are connected with no cycles.

            This is achieved by implementing a Data structure called Union-Find or Disjoint set. This data structure does 2 things:
                - Find
                    Finds the root of the node or its representative by calling the function over again until it is found.
                    This allows us to find the cycles that happen in the graph to avoid them.
                - Union
                    This unites 2 sets of data by rank (merge), this is necessary because then it stops from connecting 2 things that were already
                    connected, meaning less errors for this algo
            
            Using this data structure we can properly use this algo to its full capacity as explained below in the code
            

    Advantages of Graphs:
        + Used in many avenues including Machine Learning, Network Analysis, PathFinding, etc
        + Used to represent complex data in a simple way 
        + The algorithms are very efficient and quick 

    Disadvantages of Graphs:
        - Need to be familiar to understand
        - if large data sets, it is more complex to operate
        - If large data sets, complex to view
'''
#IM LATE WITH CODE FUUUUCK ----------------------------------------------------
'''
#Graph DS Operations ---------------
class graph:
    def __init__(self):
        self.graph = {}                         #Creates the graph (constructor) into a dictionary 

    def addVertex(self,vertex):                 #Adds the Vertex
        if vertex not in self.graph:            #if the vertex is no in the graph it will add it to the graph
            self.graph[vertex] = []             #adds the vertex as the key and anything inside is its values/adjacent to
    
    def addEdge(self, vertex1, vertex2, directed = False):
        if vertex1 not in self.graph:           #if the vertex does not exist it will call the addVertex func
            self.addVertex(vertex1)
        if vertex2 not in self.graph:
            self.addVertex(vertex2)

        self.graph[vertex1].append(vertex2)     #adds the vertex2 to the key of vertex1 to show that they are connected
        if not directed:
            self.graph[vertex2].append(vertex1)     #same thing if not directed but other way around
    
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
    visited = set()                             #Creates a set called visited (a set can not have duplicate values)
    visited.add(start)                          #adds the start value to the set
    queue = deque([start])                      #adds the start value to the queue
    while queue:                                
        vertex = queue.popleft()                #vertex = the popped value in the queue (removed) in this case it would be start
        print(vertex, end = " ")                #prints out the vertex with a space at the end
        for neighbor in graph[vertex]:          #for every neighbour in the current vertex key
            if neighbor not in visited:         #if it is not in visited, 
                visited.add(neighbor)           #it will be added to visited
                queue.append(neighbor)          #and it will be added to the queue
                                                #the process will repeat until the queue is empty (meaning when all the neighbours are in visited)

def hasCycle(graph, vertex, visited, parent):   #Checks if there is a cycle
    visited.add(vertex)                         #adds the vertex to the set of visited
    for neighbour in graph[vertex]:             #for every neighbour of the specific vertex/node
        if neighbour not in visited:            #it will check if it is not in visited and - if not - recall the func to do it again
            if hasCycle(graph, vertex, visited, parent):
                return True                     #if the func is true it will return true
            elif parent != neighbour:           #if the func is false but the parent is not a neighbour then it will return true
                return True
        return False                            #if neither requirements are met  it will return false
    
def containsCycle(graph):
    visited = set()                             #Creates a set called Visited
    for vertex in graph:                        #for every node in the graph
        if vertex not in visited:               #if the vertex/node is not in the visited it will call the hasCycle func
            if hasCycle(graph,vertex,visited,None):
                return True                     #if the func returns true then there is a cycle and it returns true    
        return False                            #If the func is not true it will return false and that means there is no cycle
    
def shortestPath(graph, start, goal):
    visited = set()                             #creates a set called visited
    queue = deque([(start, [start])])           #creates a queue with a tuple element that consists of the start vertex and value of the start vertex (this will be used for the path later)
    while queue:                                #while the queue has variables/elements:
        (vertex, path) = queue.popleft()        #the queue pops left (removes the first value in) and assigns it to the tuple of vertex and path
        for neighbour in graph[vertex]:         #for every neighbour in the key vertex:
            if neighbour not in visited:        #if it is not in visited it will check,
                if neighbour == goal:           #if the neighbour is the goal we need to reach and if so it will return the
                    return path + [neighbour]   #path and the neighbour
                else:                           #if it is not the goal then it will 
                    visited.add(neighbour)      #add the neighbour to the visited set and
                    queue.append((neighbour, path + [neighbour]))   #appends the neighbour, and the path + neighbour to the queue
    return None                                 #repeats the process until the neighbour is the goal or the queue is empty
                                                #if the queue becomes empty and the goal was not reached it will return None

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
        self.graph[u].append((v, weight))       #append 2 values under the u key and they are the node v and the weight between them (made into a tuple)
        self.graph[v].append((u, weight))       #appends 2 values under the v key and they are the node u and the weight between them (made into a tuple)
    
    def printGraph(self):                       #prints out the graph in a specific way
        for node in self.graph:                 #for each node in the graph it will print 
            print(f"{node} -> {self.graph[node]}")

#Prim's Algo ----------------
    def prims(self, start):
        mst = []                                                #Creates list for the minimum spanning tree               
        visited = set()                                         #creates set which will contain all the vertices visited
        minHeap = [(0,start,None)]                              #min heap adds a tuple that contains the weight (0) the current vertex (start)
                                                                #and from vertex (none) to its list
        while minHeap:
            weight, currentVer, fromVer = heapq.heappop(minHeap)    #these values are then popped from the minHeap and assigned to their respective variables

            if currentVer in visited:                           #if the current Vertex is visited then continue normally
                continue
            visited.add(currentVer)                             #if not then we add the current vertex to the visited set

            if fromVer is not None:                             #if the from vertex is not none then we append a tuple that contains the from vertex,
                mst.append((fromVer,currentVer,weight))         #the current vertex, and the weight between them to the mst list
            for neighbour, edgeWeight in self.graph[currentVer]:    #in graph, we previously made it into a dictionary that holds the current vertex's neighbour and 
                if neighbour not in visited:                    #the weight between them. Now for every one of those, if the neighbour is not in visited;
                    heapq.heappush(minHeap, (edgeWeight, neighbour, currentVer))    #the edge weight, neighbour, and the current vertex are pushed into the minHeap list as a tuple
                                                                                    #and the process repeats once again for as long as min heap is true (has a variable in it)
        return mst                                              #returns the minimum spanning tree list as the result


#Dijkstra Algo --------------
import heapq 

def dijkstra(graph,start):
    queue = []                                                  #Creates a queue list
    heapq.heappush(queue,(0,start))                             #This func pushes (adds) 0 and our start value to the list called queue while maintaining a proper heap
    distances = {vertex: float('inf') for vertex in graph}      #creates a dictionary with a vertex key for each vertex in the graph with a float value inside  
    distances[start] = 0                                        #gives the key start a value of 0
    visited = set()                                             #creates a set called visited

    while queue:                                                #while the queue is true
        currentDis, currentVer = heapq.heappop(queue)           #the current distance is = to the smallest value in the queue (that value is then removed). Same process is done for current vertex
        if currentVer in visited:                               #if the current vertex is in visited then continue 
            continue
        visited.add(currentVer)                                 #if not in visited then add the vertex to visited

        for neighbour, weight in graph[currentVer]:             #for each neighrbour and weight in key currentVer
            distance = currentDis + weight                      #distance is calculated as the current distance + the weight of the new edge
            if distance < distances[neighbour]:                 #if the distance calculated is less then the distance already calculated 
                distances[neighbour] = distance                 #then it will be the new distance
                heapq.heappush(queue, (distance,neighbour))     #this distance is then pushed into the queue along with the neighbour associated with it
    return distances                                            #returns the distances dictionary
'''
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
'''

#Kruskal's Algo ----------------------
class unionFind:
    def __init__(self,size) -> None:
        self.parent = list(range(size))                         #Creates a list with the size of another tree              
        self.rank = [0]* size                                   #creates a ranking list with the same size
    
    def find(self, node):
        if self.parent[node] != node:                           #if the index is not the same as the node value:
            self.parent[node]=self.find(self.parent[node])      #then that index will equal to another search
        return self.parent[node]                                #this will keep occurring until they are equal and then it will
                                                                #return the representative (the index == to value)

    def union(self,i,j):
        root1 = self.find(i)                                    #root1 becomes representative of value i
        root2 = self.find(j)                                    #root2 becomes representative of value j
        if root1 != root2:                                      #if they are not equal:
            if self.rank[root1]>self.rank[root2]:               #if the rank of root1 is more than the rank of root2:
                self.parent[root2] = root1                      #root2's element will equal to root1's value
            elif self.rank[root1]<self.rank[root2]:             #if the rank of root1 is less than the rank of root2:
                self.parent[root1] = root2                      #root1's element will equal to root2's value
            else:                                               #if they are equal:
                self.parent[root2] = root1                      #root2's element will equal to root1's value
                self.rank[root1]+=1                             #root1's rank increments by 1

class graph:
    def __init__(self, vertices):
        self.v = vertices                                       #instead of the previous graph using a dictionary,
        self.graph = []                                         #this one uses v for vertices and a list for the edges

    def addEdge(self,u,v,weight):                               
        self.graph.append((weight, u,v))                        #adds the weight of the edge and the vertices connected to it as a tuple

    def kruskal(self):
        self.graph.sort()                                       #sorts the edges in a ascending order (from smallest to biggest)
        uf = unionFind(self.v)                                  #creates a unionFind data structure with the size of self.v

        mst = []                                                #creates a minimum spanning tree list
        mstWeight = 0                                           #and a weight total for it as well starting at 0

        for edge in self.graph:                                 #for each edge in the self.graph:
            weight, u , v = edge                                #the weight and the vertices are all equal to the edge (the tuple added)
            if uf.find(u) != uf.find(v):                        #if the finds are not equal: (checks if they are a cycle or not)
                uf.union(u,v)                                   #it unites them, with the same process above (in unionFind)
                mst.append(edge)                                #then it appends the edge to the mst list
                mstWeight += weight                             #the total weight increments by the new weight 
        
        return mst, mstWeight                                   #returns both the minimum spanning tree list and the total weight
    
g = graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print("\n",g.graph,"\n")

mst, mst_weight = g.kruskal()
print("Edges in MST:", mst)
print("Total weight of MST:", mst_weight)
