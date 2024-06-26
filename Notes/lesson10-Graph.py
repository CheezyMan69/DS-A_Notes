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

g = graph()
g.addEdge('A','B',1)
g.addEdge('A','C',4)
g.addEdge('B','C',2)
g.addEdge('B','D',5)
g.addEdge('C','D',1)

g.printGraph()
