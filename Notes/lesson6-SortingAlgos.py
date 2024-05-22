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

        Advantages
            + Simple to implement
            + Stable Algorithm
            + Fast for small lists
            + Space effcient
        
        Disadvantages
            - Not good for big lists

    - Bubble Sort
        Takes 2 values and swaps them, checks if the 1st value is bigger than the 2nd value.
        If so they swap, then that value gets compared with the next value and repeats until the array ends.
        It take one value at a time, that value gets compared with all until it is smaller than the one after and it stays
        in that position.

        Advantages
            + Easy to understand
            + No need for additional Memory space

    - Selection Sort
        Trys to find the smallest value and swaps it with the first element of the unsorted part.
        Repeated untill all is sorted.
    - 
    - 
    - 
    -
    -
    -


'''
#Code ------------------------------------------------------------------------------
'''
#Insertion Sort --------------------
def insertSort(arr):
    for i in range(1,len(arr)):         #for(i=1;i<n;i++)          Time complexity calc  ->                                                     Time = O(n)
        key = arr[i]                    #Key is assigned to value 1                                                                             Time = O(1)    
        j=i-1                           #j is 0                                                                                                 Time = O(1)                    
        while j>=0 and key<arr[j]:      #when j<=0 and the key is smaller than the j value, the while loop starts                               Time = O(n) dep on i so *
            arr[j+1]=arr[j]             #Key (j+1) and J value swap                                                                             Time = O(1)
            j-=1                        #J decrements by 1 (if -1 then loop ends, if not it continues to compare over and over until j = -1)    Time = O(1)   
        arr[j+1]=key                    #when while loop ends, j+1 becomes the key value, and then it repeats for all iterations                Time = O(1)
                                        #                                                                                                       Total -> [O(n)*O(1)*O(1)*O(n)*O(1)*O(1)] -> O(n^2)

#arr = [84,39,583,239,542,245,1,69]

size=int(input("Enter the size of the array: "))

arr=[]
for _ in range(size):
    value = int(input("Enter a Value: "))
    arr.append(value)

print("Unsorted array: ",arr)
insertSort(arr)
print("Sorted array: ",arr)
'''
'''
#Bubble Sort -----------------------
def bubSort(arr):
    n=len(arr)                                      #Time -> O(1)      
    for i in range(n):                              #Time -> O(n)   This i is for the amount of values in the array
        for j in range(0,n-i-1):                    #Time -> O(n)   J is the value itself that gets checked and swapped 
                                                    #               (it goes to n-i-1 because we get the largest element to the last position in the array & we dont need to check it again)
            if arr[j]>arr[j+1]:                     #Time -> O(1)   Checks if the value is bigger than the next one
                arr[j],arr[j+1]=arr[j+1],arr[j]     #Time -> O(1)   If that is true it swaps them and then the J loop works again
                                                    #               If it is false then the loop breaks
                                                    #               Once J loop is done I loop increments and the J loop starts again
                                                    #               When i is finished completly the whole array is sorted
                                                    #
                                                    #Total  -> O(1)+[O(n)*O(n)*O(1)*O(1)]
                                                    #       -> O(n^2)

#arr = [84,39,583,239,542,245,1,69]

size=int(input("Enter the size of the array: "))

arr=[]
for _ in range(size):
    value = int(input("Enter a Value: "))
    arr.append(value)

print("Unsorted array: ",arr)
bubSort(arr)
print("Sorted array: ",arr)
'''

#Selection Sort --------------------
def selectSort(arr):
    n=len(arr)                                  #Time -> O(1)                         
    for i in range(n):                          #Time -> O(n)   
        min = i                                 #Time -> O(1)   Makes the minimum value the i value (if i =0 then its the first value)
        for j in range(i+1,n):                  #Time -> O(n)   This j loop checks if there is something smaller than our min value
            if arr[j]<arr[min]:                 #Time -> O(1)   if it is true, then the min becomes that new value then j loop ends (it runs again until n is reached)
                min = j                         #Time -> O(1)   If false then min stays the same then j loop ends (it runs again until n is reached)
        arr[i],arr[min] = arr[min], arr[i]      #Time -> O(1)   the i value and the min value swap to have the smallest value in the beginning of the array
                                                #               This repeats until i reaches n (which is the end of the array)
                                                #               Once it is over it is fully sorted
                                                #
                                                #Total  ->  O(1)+[O(n)*O(1)*O(n)*O(1)*O(1)*O(1)]
                                                #       ->  O(n^2)

#arr = [84,39,583,239,542,245,1,69]

size=int(input("Enter the size of the array: "))

arr=[]
for _ in range(size):
    value = int(input("Enter a Value: "))
    arr.append(value)

print("Unsorted array: ",arr)
selectSort(arr)
print("Sorted array: ",arr)
