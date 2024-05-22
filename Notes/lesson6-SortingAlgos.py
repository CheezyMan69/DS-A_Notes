#Notes -----------------------------------------------------------------------------
'''
What are Sorting Algorithms?
They are Algorithms that take data as an input, and sort them in a certain way, like:
    - Size
    - multiples
    - true or not
    - etc

There are multiple types of Sorting Algorithms:
    - Insertion Sort
        What it does is that it assigns the values to a key (starts at 1 not 0), this key compares itself
        with the previous value (j) and if it is larger than the previous it stays in the same place, 
        if it is smaller then they swap with one another and j=-1 exiting the while loop (example of it in code below)
    - 
    - 
    - 
    - 

'''
#Code ------------------------------------------------------------------------------

#Insertion Sort --------------------
def insertSort(arr):
    for i in range(1,len(arr)):         #for(i=1;i<n;i++)
        key = arr[i]                    #Key is assigned to value 1
        j=i-1                           #j is 0
        while j>=0 and key<arr[j]:      #when j<=0 and the key is smaller than the j value, the while loop starts
            arr[j+1]=arr[j]             #Key (j+1) and J value swap
            j-=1                        #J decrements by 1 (if -1 then loop ends, if not it continues to compare over and over until j = -1)
        arr[j+1]=key                    #key becomes a new value

#arr = [84,39,583,239,542,245,1,69]

size=int(input("Enter the size of the array: "))

arr=[]
for _ in range(size):
    value = int(input("Enter a Value: "))
    arr.append(value)

print("Unsorted array: ",arr)
insertSort(arr)
print("Sorted array: ",arr)