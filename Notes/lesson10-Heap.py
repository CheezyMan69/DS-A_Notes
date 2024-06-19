#Notes ------------------------------------------------------------------------
'''
Heap Data Structures:
    - Heap is a complete binary tree data structure that uses something called the Heap Property 
      
      + Heap Property: for each parent node the value of its children is either greater or
        lesser than to its own value (Heap property) 

    - 2 types of heap = max or min heap
        Max heap has the root node as the maximum value in the tree and all the other values are less than it
        Min heap has the root node as the minimum value in the tree and all the other values are more than it

    - Diffrences between Heap and Trees
        - Heap is a kind of tree but a tree is not a kind of heap
        - Heap has only 2 types while trees have many types
        - Heap is ordered, a normal tree is not
        - Insert and remove takes O(log n) due to the sorting and a tree only takes O(n)
        - finding max/min is O(1) due to it being the root and in a tree it takes O(log n) due to searching
        - Heap can also be referred to as PRIORITY QUEUE (a tree is a connected undirected graph with no circle [more on that later])
        - Heap is built faster than trees
        
    - Applications of Heap Data Structures
        - Prim's Algorithm (fuck this man[hate it{very not fun}]) (some shit to do with distance and traversal)
        - Dijkstra's Algorithm




'''
#CODE AGAIN -------------------------------------------------------------------

#Heap ------------------------------
class maxHeap:
    def __init__(self,array=None):
        if array is None:                               #the constructor (maker of the heap)
            self.heap = []                              #if the array does not exist, it creates one
        else:
            self.heap=array                             #if there is an array, the array becomes the heap
            self.heapify()                              #calls the heapify function to keep the heap property (check notes boss)
    
    def heapify(self):
        for i in range(len(self.heap)//2 -1,-1,-1):     #Heapify trys to find the index of the leaf nodes and calles bubble down
            self._bubbleDown(i)                         #calles bubble down with index of the value of i (more on this below)
        
    def insert(self,value):
        self.heap.append(value)                         #for each value inserted it will add to the heap array
        self._bubbleUp(len(self.heap)-1)                #calls bubble up with index of the length of the array -1 (more on this below)

    def traverse(self):
        return self.heap                                #Returns all the sorted values of the array
    
    def _bubbleUp(self,index):                          #moves the nodes up (swaps parent node with child node if not working with heap property)
        parentIndex = (index -1)//2                     #grabs the parent node of the current node
        if index > 0 and self.heap[index] > self.heap[parentIndex]:     #if the node value is bigger than the parent value they will swap
            self.heap[index],self.heap[parentIndex]=self.heap[parentIndex],self.heap[index]
            self._bubbleUp(parentIndex)                 #calls bubble up again until the root
        
    def _bubbleDown(self,index):                        #moves the node down from the root (checks if the values work with heap property)
        leftChild = 2*index +1                          #index is the current parent node and it sets the children
        rightChild = 2*index +2
        largest = index                                 #largest is the parent node in the max heap
        
        if leftChild < len(self.heap) and self.heap[leftChild]>self.heap[largest]:
            largest = leftChild                         #if the left child has a bigger value than the parent, the largest node will go to the left child
        if rightChild< len(self.heap) and self.heap[rightChild]> self.heap[largest]:
            largest = rightChild                        #if the right child has a bigger value than the parent, the largest node will be the right child


        if largest != index:                            #if the largest node now (after the checks) is not the parent node anymore, the nodes will swap to keep the heap property
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]

    def extractMax(self):
        if len(self.heap) == 0:                         #if the length of the array 0 then it does not work
            return None
        if len(self.heap) == 1:                         #if the length of the array is equvilant to 1 it will extract the first value
            return self.heap.pop()
        maxValue = self.heap[0]                         #if the length is more than 1, the max value becomes the first value (root)
        self.heap[0] = self.heap.pop()                  #then the root is extracted/deleted from the array
        self._bubbleDown(0)                             #then the bubble down is called to sort the heap once more
        return maxValue                                 #returns the max value which was the previous root
    
    def peek(self):                                     #this function looks (takes a peek at) the maximum value
        return self.heap[0] if self.heap else None      #return the root if the heap exists and if it does not then return nothing (None)
    
    def delete(self,value):
        try:                                            #Attepmts the code in the try block and if there is an error (anywhere) it will move to another code (catch block [in python its except])
                                                        #the catch block (except in python) will handle the error accordingly (telling the user to try again for example [its another code that you write])
            index = self.heap.index(value)              #index becomes the index of the value entered
            if index == len(self.heap) -1:              #if the index is equivilant to the length of the heap (array) -1 (the last element) it will delete it
                self.heap.pop()
            else:
                self.heap[index] = self.heap.pop()      #if not last element it will delete the value entered
                if index < len(self.heap):              # if the index is less than the length it will heapify again to sort the heap properly
                    self._bubbleDown(index)
                    self._bubbleUp(index)
        except ValueError:                              #if the value does not exist it will skip the try block and execute the code in the except block
            print("Value ", value," was not found in the heap ")
            

    def __str__(self):
        return str(self.heap)
    
heap = maxHeap()
values = [10,20,15,30,40,50,70,5,25,8]
for value in values:
    heap.insert(value)

print(f"Heap after Insertion: {heap}")

