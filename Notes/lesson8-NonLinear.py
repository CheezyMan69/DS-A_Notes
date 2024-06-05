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
                Moves from the highest level to the deepest level
                prints/displays the order of the values in that way

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
class treeNode: 
    def __init__(self,value):
        self.value = value                  #Creats a Node with a value
        self.children = []                  #And the list of its children

    def addChild(self,childNode):
        self.children.append(childNode)     #Adds the childNode to children in a node

    def dfs(self):
        print(self.value, end= ' ')
        for child in self.children:
            child.dfs()
    
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