#Notes -----------------------------------------------------------------------------
'''
Non-Linear Data Structures are data structures with multiple branches (like a tree[foreshadowing]),
they use a hierarchy to sort (on multiple levels[branches]). Uses classes and objects 

- Tree Data Structures
    They work on nodes, different nodes on different/multiple levels. Some Terminology that help explain what a tree is:
        - Parent nodes 
            It is a node that creates/leads into 1 or more nodes in the next level
        
        - Child Nodes
            They are the nodes that originate from a parent node 
        
        - Root Node
            A root is where the tree originates, it is a parent node because all other nodes are its children
            but it does not have a parent node
        
        - Leaf Node (External Node)
            This type of node is a child node but not a parent node (no connection/path to the next level)
            usaully on the last level of the tree
       
        - Ancestor of a Node
            Any node that leads to the target node is an ancestor meaning if node A leads to B then C
            then node A is an ancestor of node C

        -Descendant of a Node
            Similar to the ancestor but fliped. It is a node that can be traced back to from the target node
            eg) A-> B -> C -> D (D is the descendant of A)

        - Sibling
            Child nodes that are from the same parent node are sibling nodes

        - Level of a Node
            A level can be determined by the amount of edges between the nodes. Root is on Level 0
            Eg) A -> B -> C -> D    A = Level 0, B = L1, C = L2, D = L3

        - Internal Node
            A node with at least 1 child (root node and parent nodes are also internal nodes)

        - Neighbour of a Node
            When a node is connected to other nodes, these other nodes are also considered as Neighbours

        - SubTree
            A mini tree inside the main tree consists of at least one parent node and its children

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
                       repeats itself (R->C1->C1.1->C1.2->C2->C2.1->C2.2->C3->C3.1)

                Explores to the deepest level of the branch before it back tracks to the next branch

                Ways of printing this Traversal depends on the type of tree

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
            It is the longest path from the node to a leaf node (a node without children) (path = edges) 

        - Height of a Tree
            The longest path form the root to a leaf node

        - Degree of a Node
            The total count of subtrees attached to that node. The degree of a leaf node is = 0 and the degree of the tree would be the maximum degree amongst
            all the nodes
    
    Applications of Tree Data Structures (Tree DS):
        - File System
        - Data Compression
        - Compiler Design
        - Database Indexing
    
    Advantages of Tree DS:
        + Efficient Search (if balanced) -> Time complexity = O(log n)
        + Easy to Organize and navigate
        + Easy traverse

    Disadvantages of Tree DS:
        - When a tree is unbalanced, the search is inefficent 
        - A lot of memory space is taken 
        - Not easy to change cuz they complex (lol [they are trust me {sometimes at least}])

    Types of Trees:
        This is based on the number of children
        - Binary tree
            One Parent node has a maximum of 2 children
            Types of Binary tree:
                - Full Binary Tree        -> all nodes (other than the leaf nodes) have 2 children
                - Complete binary Tree    -> All levels are completly filled except the last level which is filled from left to right
                - Perfect Binary tree     -> All parent nodes have 2 children and all levels are complete from left to right
                - Incomplete Binary Tree  -> does not fill all the levels
                - Binary Search Tree(BST) -> A tree that is organized with the left side smaller than the root and specific parent node and the right side is 
                                             bigger than the root and specific parent node in values
                - Balanced Binary Tree    -> The height of left and right subtrees only differs by one between each node
                - Red Black tree          -> Self balancing binary search tree where the nodes are coloured red or black to make sure that it is balanced when
                                             deleting or insertion 
                - AVL Tree                -> Also a self balancing binary search tree where the diffrence between left and right subtrees cannot be more than
                                             one for all nodes

            Binary Operations:
                - Create -> creating a tree in the data structure
                - Insert -> Inserts data into the tree
                - Search -> Searches the tree to find specifc data
                - DFS:
                    - Pre order Traversal:
                        current -> left -> right 
                    - Inorder Traversal
                        left -> current -> right
                    - Postorder Traversal
                        left -> right -> current
                - BFS: 
                    - Level Order Traversal
            
            Advantages
                + Efficient Search -> O(n)
                + Memory Efficient
                + Easy to implement -> only 2 children

            Disadavantages
                - Limited to only 2 children
                - Could lead to unbalanced trees
                - Space taker (needs a lot of memory space)
                - Slow in worst case scenario -> O(n) (n num of nodes)

            Applications
                = Represent Hierararchial data (file system)
                = A version of the Binary tree called the Huffman coding tree is used in data compression Algos
                = Prioiry Queue is used to search for a max or min value in O(1) time
                = Used to make decision trees which is used for machine learning 

            Binary Search Tree (BST):
                This is a type of binary tree that splits values by how big or small they are compared to the root node
                - On the left of the root we will find values less than the root value
                - on the right of the root we will find values more than the root value
                This process subs the parent node instead of the root node if there are more values and then contiues to sort

                A BST handles duplicates by either putting them in the left child or the right child
                    it does not alternate 
                    eg) if value<self.value:
                            self.left = insert(self.left, value)
                        else
                            self.right = insert(self.right, value)      #this line shows that  if the value is equal to or more than self.value
                                                                         it will go to the right child meaning duplicates as well


        - Ternary tree
            A tree where the parents have 3 children max
                - Left Child
                - Middle Child (always forgotten)
                - Right Child
            
            Ternary Operations:
                - Create -> creating a tree in the data structure
                - Insert -> Inserts data into the tree
                - Search -> Searches the tree to find specifc data
                - DFS:
                    - Pre order Traversal:
                        current -> left -> right 
                    - Inorder Traversal
                        left -> current -> right
                    - Postorder Traversal
                        left -> right -> current
                - BFS: 
                    - Level Order Traversal


        - Generic or N-ary Tree
            A tree where the parents can have as many children as they want (boomers)   (same here boss after stats)


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
'''
'''
#Types of Binary Trees ------------------------------------

class treeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#Full Binary tree ------------------
def isFullBinaryTree(node):             #a quick checker to see if it is full or not
    if node is None:
        return True
    if node.left is None and node.right is None:        
        return True
    if node.left is not None and node.right is not None:
        return isFullBinaryTree(node.left) and isFullBinaryTree(node.right)
    return False

root = treeNode(1)                 #             1
root.left = treeNode(2)            #           /   \    
root.right = treeNode(3)           #          2     3
root.left.left = treeNode(4)       #         / \     
root.left.right = treeNode(5)      #        4   5     

print("Is the tree a Full Binary tree? -> ", isFullBinaryTree(root))
'''
'''
#Complete Binary Tree --------------

from collections import deque

class treeNode:
    def __init__(self,value):           
        self.value = value
        self.left = None
        self.right = None

def isCompBinaryTree(root):             #[WRONG fucking checker (fun) will change later]
    if not root:
        return True
    queue = deque([root])
    reachedEnd = False
    while queue:
        node = queue.popleft()          #same logic as the Breadth first Search using queues
        if node:                        #uses queues and if the value = none then reachedEnd = True 
            if reachedEnd:              #if there was a value after reachedEnd is True the func will return false because leafs not on
                                        #the same level
                return False            
            queue.append(node.left)
            queue.append(node.right)
        else:
            reachedEnd = True           
    return True

root = treeNode(1)                 #              1
root.left = treeNode(2)            #           /     \    
root.right = treeNode(3)           #          2       3
root.left.left = treeNode(4)       #         / \     /   
root.left.right = treeNode(5)      #        4   5   6  
root.right.left = treeNode(6)      #


print("is it a complete biary tree? ",isCompBinaryTree(root))
'''
'''
#Perfect Binary Tree ---------------
class treeNode:
    def __init__(self,value):           
        self.value = value
        self.left = None
        self.right = None

def isPerfectBinTree(node,depth,level=0):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return depth == level+1
    if node.left is None or node.right is None:
        return False
    return isPerfectBinTree(node.left,depth,level+1) and isPerfectBinTree(node.right,depth, level+1)

def findDepth(node):
    d = 0 
    while node is not None:
        d+=1
        node = node.left
    return d

root = treeNode(1)                 #              1
root.left = treeNode(2)            #           /     \    
root.right = treeNode(3)           #          2       3
root.left.left = treeNode(4)       #         / \     / \  
root.left.right = treeNode(5)      #        4   5   6   7   
root.right.left = treeNode(6)      #
root.right.right = treeNode(7)

depth = findDepth(root)
print("is perfect Binary tree? ", isPerfectBinTree(root,depth))
'''
'''
#Binary Tree Operations -----------------------------------
class treeNode:
    def __init__(self,value):          
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):                        #Time Complexity = O(n)
    if root is None:                            #if the root is none the first value will be the root value
        return treeNode(value)
    if value< root.value:
        root.left = insert(root.left, value)    #if there is a value in root and the value is more it will insert it in the left node
    else:
        root.right = insert(root.right, value)  #if the value is smaller than the root it will insert in the right node
    return root

#DFS Traversal ways ----------------
def preOrderTrav(root):                         #Time -> O(n)
    if root:
        print(root.value, end=' ')
        preOrderTrav(root.left)                 #current -> left -> right
        preOrderTrav(root.right)

def inOrderTrav(root):                          #Time -> O(n)
    if root:
        inOrderTrav(root.left)
        print(root.value, end = ' ')            #left -> current -> right
        inOrderTrav(root.right)

def postOrderTrav(root):                        #Time -> O(n)
    if root:
        postOrderTrav(root.left)
        postOrderTrav(root.right)               #left -> right -> current
        print(root.value, end=' ')

#BFS Traversal way -----------------
from collections import deque                   #Time -> O(n)
def levelOrderTrav(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end = ' ')
        if  node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

#root = treeNode(10)
#values = [5,15,3,7,12,18]
#
#           10
#        /      \   
#       5        15
#      / \      /  \ 
#     3   7    12  18
#
size = int(input("Enter the amount of Nodes in the tree: "))
values=[]

rootVal = int(input("Insert the Root value: "))
root = treeNode(rootVal)

for _ in range(size-1):
    value = int(input("Insert value: "))
    values.append(value)

for value in values:
    root = insert(root, value)


print(" ---Preorder Traversal--- ")
preOrderTrav(root)
print()

print(" ---Inorder Traversal--- ")
inOrderTrav(root)
print()

print(" ---Postorder Traversal--- ")
postOrderTrav(root)
print()

print(" ---Level Order Traversal--- ")
levelOrderTrav(root)
print()
'''

#Binary Search Tree -----------------------------
class treeNode:
    def __init__(self,value):                   #Initializes (constructs) the tree
        self.value = value      
        self.left = None
        self.right = None

def insert(root, value):                        #Time Complexity = O(n)     Inserts values into the tree
    if root is None:                            #if the root is none the first value will be the root value
        return treeNode(value)
    if value< root.value:
        root.left = insert(root.left, value)    #if there is a value in root and the value is more it will insert it in the left node
    else:
        root.right = insert(root.right, value)  #if the value is smaller than the root it will insert in the right node
    return root

def search(root,value):                         #Searches the tree to fina a specific value
    if root is None or root.value == value:     #if the root value is nothing or is the value we are searching for it will return it
        return root
    if value < root.value:                      #if the value is less than the root it will search the left part of the tree until it reaches it
        return search(root.left,value)
    else:                                       #if value is bigger than the root it will search the right part of the tree until it reaches it
        return search(root.right,value)
    
def findMin(node):                              #this function is too find the last node in the tree
    current = node                              #makes the current node the root
    while current.left is not None:             #while the node.left is not empty the current becomes the left then checks again 
        current=current.left                    #then repeats the process until left is none (current for example can be current.left.left.left)
    return current                              #once the while loop is over it returns the final current

def delete(root,value):                         #To delete specific values
    if root is None:                            #If the root is empty it will not delete anything and returns the empty root
        return root
    if value < root.value:                      #if the value is lower than the root then it will search for the value in root.left
        root.left = delete(root.left,value)     
    elif value > root.value:                    #if the value is larger than the root then it will search for the value in root.right
        root.right = delete(root.right,value)
    else:
        if root.left is None:                   #if root.left is empty it will return the root.right and vice versa
            return root.right
        elif root.right is None:
            return root.left
        temp = findMin(root.right)              #a temp variable is used to hold the min node root.right
        root.value = temp.value                 #the specific root's value becomes the temp value 
        root.right = delete(root.right,temp.value)  #this calls the function again but this time with the root and the temp value to remove them
    return root                                 #returns the root

def preOrderTrav(root):
    if root:                                    #if root is not empty it displays like this: C->L->R
        print(root.value, end=' ')
        preOrderTrav(root.left)
        preOrderTrav(root.right)

def inOrderTrav(root):
    if root:                                    #if root is not empty it displays like this: L->C->R
        inOrderTrav(root.left)
        print(root.value, end=' ')
        inOrderTrav(root.right)

def postOrderTrav(root):
    if root:                                    #if root is not empty it displays like this: L->R->C
        postOrderTrav(root.left)
        postOrderTrav(root.right)
        print(root.value,end=' ')

root = None
#values = [8,5,2,7,6,12,9,16,13,10]

#kinda behind on the code had to deal with council shit ill catch up

size = int(input("Enter the amount of Nodes in the tree: "))
values=[]

for _ in range(size):
    value = int(input("Insert value: "))
    values.append(value)

for value in values:
    root = insert(root,value)

printway = input("How would you like this to be printed? (I = Inorder | Pre = Preorder | Po = Postorder): ")
if printway == 'I' or printway == 'i':
    print(" ---Inorder Traversal--- ")
    inOrderTrav(root)
    print()

if printway == "pre" or printway =="Pre" or printway == "PRE" or printway == "PRe" or printway == "pRE" or printway == "pRe" or printway == "prE":
    print(" ---Preorder Traversal--- ")
    preOrderTrav(root)
    print()

if printway == "po" or printway == "Po" or printway == "pO":
    print(" ---Postorder Traversal--- ")
    postOrderTrav(root)
    print()

searchOrDelete = input("\nSearch or delete? (S or D) ")
if searchOrDelete == "S" or searchOrDelete == "s":
    valueToSearch = int(input("\nEnter a Value you want to search for: "))
    foundNode = search(root,valueToSearch)
    if foundNode:
        print("Search for ",valueToSearch," is True")
    else:
        print("Search for ",valueToSearch," is False/Not Found")

if searchOrDelete == "D" or searchOrDelete == "d":
    valueToDelete = int(input("\nEnter a Value you want to delete: "))
    goneBye = delete(root,valueToDelete)
    if goneBye:
        print("Deleted ",valueToDelete)
    else:
        print("Failed to delete ",valueToDelete," -> (it no exist boss)")
    printway = input("How would you like this to be printed? (I = Inorder | Pre = Preorder | Po = Postorder): ")
    if printway == 'I' or printway == 'i':
        print(" ---Inorder Traversal--- ")
        inOrderTrav(root)
        print()

    if printway == "pre" or printway =="Pre" or printway == "PRE" or printway == "PRe" or printway == "pRE" or printway == "pRe" or printway == "prE":
        print(" ---Preorder Traversal--- ")
        preOrderTrav(root)
        print()

    if printway == "po" or printway == "Po" or printway == "pO":
        print(" ---Postorder Traversal--- ")
        postOrderTrav(root)
        print()

else:
    print("so you dont want to do shit got it bye bitch")

