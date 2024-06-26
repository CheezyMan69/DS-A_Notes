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

#Graph DS Operations
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

def hasCycle(graph, vertex, visited, parent):
    visited.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            if hasCycle(graph, vertex, visited, parent):
                return True
            elif parent != neighbour:
                return True
        return False
    
def containsCycle(graph):
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            if hasCycle(graph,vertex,visited,None):
                return True
        return False
    
def shortestPath(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
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