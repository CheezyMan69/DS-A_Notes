#Notes -----------------------------------------------------------------------------
'''
Non-Linear Data Structures are data structures with multiple branches (like a tree[foreshadowing]),
they use a hierarchy to sort (on multiple levels[branches]). Uses classes and objects 

- Tree Data Structures
    They work on nodes, different nodes on different/multiple levels. some nodes are
        - Parent nodes 
            They are the nodes that give access to the next level (to their children)
        - Child Nodes
            They are the nodes 

    Each tree consists of a root node and sub trees - children and parents.
    A node consits of the data inside it and its child nodes.

    Root is level 0, the first children would be level 1 and so on.

    Basic operations of Tree Structures:
        - Create -> creating a tree in the data structure
        - Insert -> Inserts data into the tree
        - Search -> Searches the tree to find specifc data
        - Travesrse:
            Depth-First-Search Traversal (DFS)
                Moves from the deepest level (most cases level 0 = root) first to the highest level:
                    1. Checks if the root as children and if so it will move from root to the first child  (R->C1)
                    2. checks if the first child has children and if so it will move to their first child  (C1 -> C1.1)
                    3. once there are no more children it will go to the sibling node (a node with the same parent on the same level) (C1.1 -> C1.2)
                    4. when there are no more siblings on that level it will go back to the parent node's level and move to their siblings and the process
                       repeats itself (R->C1->C1.1->C1.2->C2->C2.1->C2.2->C3->3.1)

                Explores to the deepest level of the branch before it back tracks to the next branch

                prints/displays the order of the values in that way

            Breadth-first-Search Traversal (BFS)
                Prints the values of each node level by level in the form of a queue:
                    -  last in first out  (Example to the right of explain)
                    1. creates a queue with the root first and appends the children to the queue                                                    [R|C1|C2|C3]
                    2. prints the root and calls the function on C1 (moves it ahead in the queue[popleft()]) so it puts its children in the queue   [C1|C2|C3|C1.1|C1.2]
                    3. Prints C1 and calls the function on the next in the queue (C2) and repeats                                                   [C2|C3|C1.1|C1.2|C2.1|C2.2]
                    4. Prints C2 and calls the function on the next in the queue (C3) the same occurs                                               [C3|C1.1|C1.2|C2.1|C2.2|C3.1]   
                    5. Prints C3 and calls the function on the next in the queue (C1.1) but due to it having no children it prints it and moves on again 
                       Loop keeps on going until all the queue is finished
    
    Properties of a Tree:
        - Number of Edges
            An edge is the link between 2 nodes. If a tree has N nodes it will have N-1 edges connecting all of them. There is only one path
            from each node to any other node in the tree.

        - Depth of a Node
            The depth is the length from the root to that node (path from root to node). it is calculated using the smallest amount of edges between them,
            each edge is one unit of length.

        - Height of a Node
            It is the longest path from the node to a leaf node (path = edges)

        - Height of a Tree
            The longest path form the root to a leaf node

        - Degree of a Node
            The total count of subtrees attached to that node. The degree of a leaf node is = 0 and the degree of the tree would be the maximum degree amongst
            all the nodes
    
    Applications of Tree Data Structures:
        - File System
        - Data Compression
        - Compiler Design
        - NOT FUCKING DONE YET WHY MOVE SO DAMN FAST

    Types of Trees:
        This is based on the number of children
        - Binary tree
        - Tireachry tree
        - N-ary Tree


'''
#Code ------------------------------------------------------------------------------
'''
#Simple Tree -----------------------
class treeNode: 
    def __init__(self,value):
        self.value = value                  #Creats a Node with a value
        self.children = []                  #And the list of its children

    def addChild(self,childNode):
        self.children.append(childNode)     #Adds the childNode to children in a node
    
    def displayTree(self,level=0):
        indent = " "*(level*4)              
        print(indent+str(self.value))
        for child in self.children:
            child.displayTree(level+1)
    
                                            #Creating a simple tree now
root = treeNode("Root")                     #Root of tree
child1= treeNode("Child 1")                 #1st child (C1)
child2= treeNode("Child 2")                 #2nd Child (C2)
child3= treeNode("Child 3")                 #3rd Child (C3)
                                            #all these children have their parent node as root

child1_1 = treeNode("Child 1.1")            #1st child of C1
child1_2 = treeNode("Child 1.2")            #2nd child of C1
child2_1 = treeNode("Child 2.1")            #1st child of C2
child2_2 = treeNode("Child 2.2")            #2nd Child of C2
child3_1 = treeNode("Child 3.1")            #1st child of C3

root.addChild(child1)
root.addChild(child2)                       #adds the rootNodes children into the children list
root.addChild(child3)

child1.addChild(child1_1)                   #adds the children of C1 to child1 node
child1.addChild(child1_2)

child2.addChild(child2_1)                   #adds the children of C2 to child2 node
child2.addChild(child2_2)

child3.addChild(child3_1)                   #adds the children of C3 to child3 node

root.displayTree()                          #displays the tree from the root so it can display the entire tree
                                            #if displayed from child1 it will only show child1 and its children (subtree of C1 only)
'''

#DFS and BFS Traversal Techniques --

from collections import deque               #For BFS (queue)

class treeNode: 
    def __init__(self,value):
        self.value = value                  #Creats a Node with a value
        self.children = []                  #And the list of its children

    def addChild(self,childNode):
        self.children.append(childNode)     #Adds the childNode to children in a node

    def dfs(self):
        print(self.value, end= ' ')
        for child in self.children:         #DFS -> prints the value of the node -> checks for children -> runs dfs on children (repeat)
            child.dfs()
    
    def bfs(self):
        queue = deque([self])
        while queue:
            node = queue.popleft()
            print(node.value, end = ' ')
            for child in node.children:
                queue.append(child)
    
root = treeNode("Root")                     #Root of tree
child1= treeNode("Child 1")                 #1st child (C1)
child2= treeNode("Child 2")                 #2nd Child (C2)
child3= treeNode("Child 3")                 #3rd Child (C3)
                                            #all these children have their parent node as root

child1_1 = treeNode("Child 1.1")            #1st child of C1
child1_2 = treeNode("Child 1.2")            #2nd child of C1
child2_1 = treeNode("Child 2.1")            #1st child of C2
child2_2 = treeNode("Child 2.2")            #2nd Child of C2
child3_1 = treeNode("Child 3.1")            #1st child of C3

root.addChild(child1)
root.addChild(child2)                       #adds the rootNodes children into the children list
root.addChild(child3)

child1.addChild(child1_1)                   #adds the children of C1 to child1 node
child1.addChild(child1_2)

child2.addChild(child2_1)                   #adds the children of C2 to child2 node
child2.addChild(child2_2)

child3.addChild(child3_1)                   #adds the children of C3 to child3 node

print("DFS Traversal : ")
root.dfs()

print("\nBFS Traversal : ")
root.bfs()