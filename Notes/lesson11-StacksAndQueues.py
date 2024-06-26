#Notes ------------------------------------------------------------------------------------
'''
Stacks
    What is a stack?
        something

    Main functions:
        - Push
            Adds elements to the top of the stack
        - Pop
            To remove the top most element in the stack
        - Peek
            To look at the top most element in the stack

Queue
    First in First out
    Last in Last out

    deque
        Removes the first element in the queue (front of queue)

    Size
        To know the size of the queue

    

'''
#Code -------------------------------------------------------------------------------------

#Stacks ----------------------------
class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
        print(f"Pushed {item}, Stack: {self.items}")

    def pop(self):
        if not self.isEmpty():
            item = self.items.pop()
            print(f"Popped {item}, Stack: {self.items}")
            return item
        else: 
            print("Pop Operation failed, Stack is empty")

    def peek(self):
        if not self.isEmpty():
            print(f"Peek {self.items[-1]}")
            return self.items[-1]
        else:
            print("Peek Operation failed, Stack is empty")

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        print(f"Size of Stack: {len(self.items)}")
        return len(self.items)
    
    def printStack(self):
        print(f"Stack: {self.items}")

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
s.isEmpty()
