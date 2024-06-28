#Notes ------------------------------------------------------------------------------------
'''
Stacks
    What is a stack?
        A linear data structure that uses the first in -> last out method which means when we add an element it will be the top-most on the stack, if 
        we then add another element, that one will be the top and the previous one (the first one in) will be underneath it/after it. When we want to 
        remove an element, the top-most element (last in) will be the one removed. 

    Main functions:
        - Push/Append
            Adds elements to the top of the stack
        - Pop
            Removes the top most element in the stack
        - Peek
            Looks at the top most element in the stack
        - Size
            Checks on the current size of the Stack
        - Is Empty?
            Checks if the stack is empty or not
        - Print
            Prints/Displays out the current Stack
    
    Advantages of using Stacks:
        + Simple to use and implement 
        + Fast for adding and/or removing elements -> Time = O(1)
        + Can be implented into other data structures such as Linked Lists
        + Used to implement undo and redo functions to the program

    Disadvantages:
        - There is a maximum size to the Stack, so large data sets are not good for this DS
        - Not fast to access elements that are not at the top
        - Can't search efficently 

Queue
    Another linear Data Structure similar to stacks but the difference is that it uses the First in -> First out method unlike stacks where it is
    First in -> Last out. This method is very similar to a proper queue at a super market for example. When we added the first element 

    Main Functions:
        - deque
            It is a double ended queue (acts both as a stack and a queue)
            Removes the first element in the queue (front of queue) using popleft()
        - Push
            Appends the new value into the end of the queue
        - Size
            Checks the size of the queue

    

'''
#Code -------------------------------------------------------------------------------------
'''
#Stacks ----------------------------
class stack:
    def __init__(self):
        self.items = []                                     #Constructs the stack as a list of items

    def push(self,item):
        self.items.append(item)                             #adds the item to the list
        print(f"Pushed {item}, Stack: {self.items}")        #displays that the item has been added as well as the stack itself

    def pop(self):
        if not self.isEmpty():                              #if not empty:
            item = self.items.pop()                         #the stack pops (removes the top most element) and assigns it to the variable item
            print(f"Popped {item}, Stack: {self.items}")    #shows that the item was succesfully popped as well as the rest of the stack
            return item                                     #returns the item 
        else: 
            print("Pop Operation failed, Stack is empty")   #if the stack is empty: it shows that nothing can be popped because of it is empty

    def peek(self):
        if not self.isEmpty():                              #if not empty:
            print(f"Peek {self.items[-1]}")                 #peeks at the item with the index of -1 (the top most element)
            return self.items[-1]                           #returns the peeked item
        else:
            print("Peek Operation failed, Stack is empty")  #if empty: it shows that nothing can be peeked at because the stack is empty

    def isEmpty(self):                      
        return len(self.items) == 0                         #if the length of the list of items is 0 then it will return true, 
                                                            #otherwise it will return false
    
    def size(self):
        print(f"Size of Stack: {len(self.items)}")          #prints the size of the stack using the length func
        return len(self.items)                              #returns the size
    
    def printStack(self):
        print(f"Stack: {self.items}")                       #prints the items in the stack (the list)

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.peek()
print("Printing Stack -> ")
s.printStack()

s.pop()
s.peek()
s.size()
print("\nIs the stack empty? ")
print(s.isEmpty())
'''

#Queues ----------------------------
from collections import deque

class queue:
    def __init__(self):
        self.items = deque()                                #Constructs the queue using deque

    def push(self, item):
        self.items.append(item)                             #appends the item to the end of the queue
        print(f"Pushed {item}, Queue: {self.items}")

    def pop(self):
        if not self.isEmpty():                              #if not empty:
            item = self.items.popleft()                     #the queue pops (removes the first element in) and assigns it to the variable item
            print(f"Popped {item}, Queue: {self.items}")    #shows that the item was succesfully popped as well as the rest of the queue
            return item                                     #returns the item 
        else:                                    
            print("Pop Operation failed, Queue is empty")   #if the queue is empty: it shows that nothing can be popped because of it is empty

    def peek(self):
        if not self.isEmpty():                              #if not empty:
            print(f"Peek {self.items[0]}")                  #peeks at the item with the index of 0 (the first element in)
            return self.items[0]                            #returns the peeked item
        else:
            print("Peek Operation failed, Queue is empty")  #if empty: it shows that nothing can be peeked at because the queue is empty

    def isEmpty(self):                      
        return len(self.items) == 0                         #if the length of the list of items is 0 then it will return true, 
                                                            #otherwise it will return false
    
    def size(self):
        print(f"Size of Queue: {len(self.items)}")          #prints the size of the queue using the length func
        return len(self.items)                              #returns the size
    
    def printQueue(self):
        print(f"Queue: {self.items}")                       #prints the items in the queue (the list)

q = queue()
q.push(1)
q.push(2)
q.push(3)
q.peek()
q.printQueue()

q.size()
q.pop()
q.pop()
q.pop()
print("\nIs the Queue empty?")
print(q.isEmpty())
