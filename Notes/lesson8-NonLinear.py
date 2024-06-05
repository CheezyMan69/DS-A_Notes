#Notes -----------------------------------------------------------------------------
'''
Non-Linear Data Structures are data structures with multiple branches (like a tree[foreshadowing]),
they use a hierarchy to sort (on multiple levels[branches]). Uses classes and objects 

- Trees
    They work on nodes, different nodes on different/multiple levels. some nodes are
        - Parent nodes 
            They are the nodes that give access to the next level (to their children)
        - Child Nodes
            They are the nodes 

    Each tree consists of a root node and sub trees - children and parents.
    A node consits of the data inside it and its child nodes.

    Basic operations of Tree Structures:
        - Create -> creating a tree in the data structure
        - Insert -> Inserts data into the tree
        - Search -> Searches the tree to find data
        - Travesrse -> 

'''
#Code ------------------------------------------------------------------------------

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

