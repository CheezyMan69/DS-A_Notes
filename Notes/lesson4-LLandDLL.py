#Notes -----------------------------------------------------------------------------
'''
Structures are a group of variables and classes and objects mimic the real world 
'''
#Recap of some DATA STRUCTURES -----
'''
    - Linked Lists (LL) = resizable, uses memory allocation to link values with one another
                            stores a value and a memory address -> the memory address is for the next value in line (Pointer)
                                This is used to get things that are far apart from one another unlike an array where they are all next to
                                one another in the memory 

    - Doubly Linked Lists (DLL) = similar to Linked Lists but instead of only a next memory address it also houses a previous memory address
                                    This allows it to go back and forth (Backwards to the previous address and Forwards to the next address)
                                         Sorting in this way is much much faster (apparently)
                                             For LL it only goes one way so more iterations for sorting but for DLL it can go back and forth so the 
                                             amount of iterations are less getting it to sort faster
                                                LL can take up to 6 iteration for sorting one list but DLL can do it in 3 iterations for the same list
'''
#Classes and Objects ---------------
'''
- Object = an object is a variable 

- Class = a class is a group of objects with an assigned set of properties 

- Inheritance = a way of merging 2 classes using the parent class, properties from here will be copied to the other classes, 
                and the child class, it receives the properties

'''
#Coding examples for each ---------------------------------------------------------
'''
#LL --------------------------------
class node:
    def __init__(self,data):                #creates a node that houses the value in data and the next node in next(added in append)
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newNode = node(data)                #every time append is called it will create a new node
        if not self.head:                   #it checks if the head is empty or not
            self.head = newNode             #if empty then it assigns the new node to the head
        else:
            current = self.head             #if filled then we track the new node with current
            while current.next:             #current is assigned to the head and then it assigns the next value to the new node
                current = current.next      #if current.next is filled current will become the previously assigned node
            current.next = newNode          #and its next will be the new node that was just created
    
    def display(self):
        current = self.head
        while current:
            print("------------")
            print("Data -> ",current.data," Next -> ",current.next, end = " -> ")
            print("------------")
            current = current.next          #display assigns current to head and then prints its data and the next value
        print("None")                       #after that is done current becomes the next node and it repeats until current.next is empty
                                            #when current.next is empty it prints "None"

sLL = singlyLinkedList()

size = int(input("Enter the size of the Linked List: "))
for _ in range(size):
    value = int(input("Enter the value for the Node: "))
    sLL.append(value)                       #calls the append function (value is data)

sLL.display()                               #calls the display function
'''
'''
#DLL -------------------------------
class node:                                 #creates a node that houses the value in data, next node address in next and last node address in previous
    def __init__(self,data):
        self.previous = None
        self.data = data
        self.next = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newNode = node(data)
        if not self.head:
            self.head = newNode
        else:
            current = self.head             #same process as LL but the previous is added
            while current.next:
                current = current.next
            current.next = newNode          #only changes next not all of current

            newNode.previous = current      #this makes the previous the last node used (current is still the last node)
    
    def display(self):
        current = self.head
        while current:
            print("------------")
            print("Previous -> ",current.previous,"\nData -> ",current.data,"\nNext -> ",current.next, end = "\n<->\n")
            print("------------")
            current = current.next  
        print("None")

dLL = doublyLinkedList()

size = int(input("Enter the size of the Doubly Linked List: "))

for _ in range(size):
    value = int(input("Enter the value for the Node: "))
    dLL.append(value)                       

dLL.display()     
'''
'''
#Reverse DLL -----------------------
class node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class reverseDoublyLinkedList:
    def __init__(self):
        self.head = None                    #instead of using current for the tracking we use head and tail
        self.tail = None                    #tail is the newest node created at the time
    
    def append(self,data):
        newNode = node(data)
        if not self.head:
            self.head = newNode
        else:
            self.tail.next = newNode        #this makes the tail's next the new node
            newNode.prev = self.tail        #this makes the new node's prev the tail (which is the last node)

        self.tail = newNode
    
    def displayRev(self):
        current = self.tail
        while current:
            print("Prev -> ", current.prev, "\nData -> ", current.data,"\nNext -> ",current.next, end = "\n----<->----\n")
            current = current.prev
        print("None")

rDLL = reverseDoublyLinkedList()

size = int(input("Enter size for the Doubly Linked List: "))

for _ in range(size):
    value = int(input("Enter value for the Node: "))
    rDLL.append(value)

rDLL.displayRev()
'''