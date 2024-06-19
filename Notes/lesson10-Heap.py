#Notes ------------------------------------------------------------------------
'''
Heap Data Structures:
    - Heap is a complete binary tree data structure that for each parent node the value of 
      its children is either greater or lesser than to its own value (Heap property)

    - 2 types of heap = max or min heap
        Max heap has the root node as the maximum value in the tree and all the other values are less than it
        Min heap has the root node as the minimum value in the tree and all the other values are more than it

    - Diffrences between Heap and Trees
        - Heap is a kind of tree but a tree is not a kind of heap
        - Heap has only 2 types while trees have many types
        - Heap is ordered, a normal tree is not
        - Insert and remove takes O(log n) due to the sorting and a tree only takes O(n)
        - finding max/min is O(1) due to it being the root and in a tree it takes O(log n) due to searching
        - Heap can also be referred to as PRIORITY QUEUE (a tree is a connec)
        - 




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
        for i in range(len(self.heap)//2 -1,-1,-1):     #?
            self._bubbleDown(i)                         #calles bubble down with index of the value of i (more on this below)
        
    def insert(self,value):
        self.heap.append(value)                         #for each value inserted it will add to the heap array
        self._bubbleUp(len(self.heap)-1)                #calls bubble up with index of the length of the array -1 (more on this below)

    def traverse(self):
        return self.heap                                #
    
    def _bubbleUp(self,index):
        parentIndex = (index -1)//2
        if index > 0 and self.heap[index] > self.heap[parentIndex]:
            self.heap[index],self.heap[parentIndex]=self.heap[parentIndex],self.heap[index]
            self._bubbleUp(parentIndex)
        
    def _bubbleDown(self,index):
        leftChild = 2*index +1
        rightChild = 2*index +2
        largest = index
        
        if leftChild < len(self.heap) and self.heap[leftChild]>self.heap[largest]:
            largest = leftChild
        if rightChild< len(self.heap) and self.heap[rightChild]> self.heap[largest]:
            largest = rightChild


        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]

    def __str__(self):
        return str(self.heap)