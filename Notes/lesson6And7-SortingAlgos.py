#Notes -----------------------------------------------------------------------------
'''
What are Sorting Algorithms?
They are Algorithms that take data as an input, and sort them in a certain way, like:
    - Numbers
    - prices
    - dates
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
            + Great for almost sorted lists
        
        Disadvantages
            - Not good for big lists
            - Not as fast or effiecent as other sorting algos

    - Bubble Sort
        Takes 2 values and swaps them, checks if the 1st value is bigger than the 2nd value.
        If so they swap, then that value gets compared with the next value and repeats until the array ends.
        It take one value at a time, that value gets compared with all until it is smaller than the one after and it stays
        in that position.

        Advantages
            + Easy to understand
            + No need for additional Memory space
            + Stable Algorithm (elements with same value keep their order in the sorted list)
        
        Disadvantages
            - Time Complexity of O(n^2) = slow for big lists
            - comparison-based algo = needs some thing to compare with to find the order. can slow down the algo

    - Selection Sort
        Trys to find the smallest value and swaps it with the first element of the unsorted part.
        Repeated untill all is sorted. (Full explaination in code below)

        Advantages
            + Fantastic at small data sets
            + Simple enough
        
        Disadvantages
            - O(n^2) for time compexity = slow for big data sets
            - Does not work for large lists
            - not stable (does not keep the order of elements with the same value)

Divde and Conquer Algorithm
    This is a type of Algorithm that splits up the problem into the smallest possible parts (subproblems).
    It then solves them independently and then merges the solution after it is done.
    This gives the solution to the bigger problem that was orginally proposed.
    This is a stratagy that some Sorting Algorithms use to make things simpler for the computer
    and save some time while doing so.

    Some Sorting algorithms that use this are:     
        - Merge Sort
            Uses the divide and conquer algo of making them the smallest possible problems/lists by halfing the 
            lists to its smallest number then it solves them (conquers them) then merges them in the end to provide 
            the solved and sorted list

            Advantages
                + Time complexity O(n log n) -> fast for big data sets
                + Stable
                + Simple (I dare to disagree)
            
            Disadvantages
                - Takes a lot of additional memory space
                - Creates more arrays to store the sorted halfs so it takes more space
        
        - Quick Sort
            Uses the divide and concquer but uses pivots and partitions. Pivots are elements that are compared within the array.
            Anything smaller than the selected pivot will go to the left side and anything that is larger will go to the right side.
            This places the pivot in the right place. This action splits the array into a left side (smaller) and a right side (larger) called partitions.
            A pivot is chosen in each and then the process is repeated (recursivly done) until it is fully sorted.
            The pivot is usally the last or first element in the array (also the same way when seperated into partitions).

            Advantages
                + Efficent on large data sets
                + Requiers small amount of memory 
            
            Disadvantages
                - Worst case has a time comlexity of O(n^2)
                - Not good for small data sets
                - Not stable (does not keep the order of the values)
        
        - Counting Sort
            This is not a divide and conquer algo, it also does NOT use comparisons. It counts the frequency of each value.
            Uses the highest value as the max. It stores values in a counting array with a size of max+1.
            It runs through the array and counts how many times the value appears and stores the frequancy in the counting array.
            The frequency is stored in the respective element. This frequency is then used as the postion for each element in the sorted
            array. 

            For example:
            2,3,5,1,3,5,6,0 -> sorted = 0,1,2,3,3,5,5,6
            max = 6
            size = 6+1 = 7
            counting algo [0,1,2,3,4,5,6]
                          [1,1,1,2,0,2,1] -> for the value 0 it appears only once so in the element index [0] the value is 1
                          [1,2,3,5,5,7,8] -> cumilative frequancy
            
            After reaching the cumilative frequancy stage, it goes back to the original array and looks at the first value.
            It then looks at the counting array and checks which position that value is in.
            It places that value in that postion (eg. 2 is in the 3rd position [num in cumilative frequancy]) then it decrements it by one.
            This action is for when the list goes back to that number, it can be put into that new position.

            Advantages 
                + Faster than all comaprison-based algos
                + Stable (keeps the order the same)
                + Easy to code (bullshit)

            Disadvantages
                - Does not work on decimals (only on whole numbers [int])
                - Not good with big values
                - Uses extra place in memory 
            
        - Bucket Sort (will be dealt with next lesson [name of file will not change tho])
    

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
                                        #                                                     Big O Notation is in Lesson5-AlgoIntro.py
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
'''
#Selection Sort --------------------
def selectSort(arr):
    n=len(arr)                                  #Time -> O(1)                         
    for i in range(n):                          #Time -> O(n)   
        min = i                                 #Time -> O(1)   Makes the minimum value the i value (if i =0 then its the first value)
        for j in range(i+1,n):                  #Time -> O(n)   This j loop checks if there is something smaller than our min value
            if arr[j]<arr[min]:                 #Time -> O(1)   if it is true, then the min becomes that new value then j loop ends 
                min = j                         #Time -> O(1)   If false then min stays the same then j loop ends 
                                                #                  - The j loop repeats until it reaches n no matter the outcome of the if statment
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
'''
'''
#Merge Sort ------------------------
def mergeSort(arr):
    if len(arr) > 1:
        half = len(arr)//2                              #// = int division (python normally uses floats)
        leftHalf = arr[:half]                           #the : indicates the direction of the array that will be focused on
        rightHalf = arr[half:]                          # :half -> before half, half: -> half and after half

        mergeSort(leftHalf)                             #calls the function again to keep spliting each half into smaller sublists
        mergeSort(rightHalf)                            #this keeps going until it cannot be divided anymore
                                                        #these function calls sort each half first before moving on using next part of the code
                                                        #once each half is sorted, it will sort them against each other and add the result to the main array
                                                        #Merge sort uses recursive functions to sort the whole array

        i=j=k=0                                         #initalizing values
        while i<len(leftHalf) and j<len(rightHalf):     #only works when both are true
                                                        #Argument -> while i is smaller than the length of the left half and j is smaller than the length of the right half

            if leftHalf[i]<rightHalf[j]:                #checks if the left half element i is smaller that the right half element j (both the first in their halfs [0])
                arr[k] = leftHalf[i]                    #if TRUE the array element k (in this case 0) will be that value
                i+=1                                    #i increments by 1 to move on to the next element on the left half
            else: 
                arr[k]=rightHalf[j]                     #if FALSE the array element k will be the value of element j in the right half
                j+=1                                    #j increments by 1 to move on to the next element on the right half

            k+=1                                        #k increment by 1 to move on to the next element in the array (outside of if else so it will occur after it)
                                                        #the while loop repeats if both arguments are true and breaks (moves on) if not

        while i<len(leftHalf):                          #only if 1 is true
            arr[k]=leftHalf[i]                          #array element k takes the value of element i in the left half
            i+=1                                        #i increments by 1 to move on to the next element in the left half
            k+=1                                        #k increment by 1 to move on to the next element in the array 
        while j<len(rightHalf):
            arr[k] = rightHalf[j]                       #array element k takes the value of element j in the right half
            j+=1                                        #j increments by 1 to move on to the next element on the right half
            k+=1                                        #k increment by 1 to move on to the next element in the array

#arr = [84,39,583,239,542,245,1,69]

size=int(input("Enter the size of the array: "))

arr=[]
for _ in range(size):
    value = int(input("Enter a Value: "))
    arr.append(value)

print("Unsorted array: ",arr)
mergeSort(arr)
print("Sorted array: ",arr)
'''
'''
#Quick Sort ------------------------
def quickSort(arr,low,high):
    if low<high:                                    #Time -> O(1)
        pivotIndex = partition(arr,low,high)        #Time -> O(1)
        quickSort(arr,low,pivotIndex-1)             #Time -> O(n)
        quickSort(arr,pivotIndex+1,high)            #Time -> O(n)
                                                    #Total -> O(1)+O(n)*O(n) = O(n^2)
def partition(arr,low,high):
    pivot = arr[high]                               #Time -> O(1)   gets the pivot to be the last element (high is the last element)
    i=low-1                                         #Time -> O(1)   i becomes the value before the first value (low)
    for j in range (low,high):                      #Time -> O(n)   lets j run from the 1st element (low) to the last element (high) (j=low;j<high;j++)
        if arr[j]<pivot:                            #Time -> O(1)   checks if the j element is smaller than the pivot 
            i+=1                                    #Time -> O(1)   if TRUE the i increments first
            arr[i],arr[j] = arr[j], arr[i]          #Time -> O(1)   and the values of j and i swap 
                                                    #               then the for loop repeats until j is at the last element (high)

    arr[i+1],arr[high] = arr[high], arr[i+1]        #Time -> O(1)   i+1 becomes the new high which is the new pivot
    return i+1                                      #Time -> O(1)   we return i+1 because its our new pivot which is used in the quick sort function

#arr = [84,39,583,239,542,245,1,69]

size=int(input("Enter the size of the array: "))

arr=[]
for _ in range(size):
    value = int(input("Enter a Value: "))
    arr.append(value)

print("Unsorted array: ",arr)
quickSort(arr,0,len(arr)-1)                         #low = 0, high = length of array - 1
print("Sorted array: ",arr)
'''
'''
#Counting Sort ---------------------
def countSort(arr):
    maxValue = max(arr)                 #Time -> O(1)   max value is the maximum value that appears i nthe array
    counts =[0]*(maxValue+1)            #Time -> O(m)   creates a counting array
    output =[0]*len(arr)                #Time -> O(n)   creates a final array

    for num in arr:                     #Time -> O(n)   count occurences of each element
        counts[num]+=1                  #Time -> O(1)   counts the frequency of each number by incrementing the element[num] by 1
    
    for i in range(1,maxValue+1):       #Time -> O(m)   update counts to contin the position of each element in the sorted array
        counts[i] += counts[i-1]        #Time -> O(1)   Calculates the cumilative frequency as seen in the explaination in [Notes]

    for num in reversed(arr):           #Time -> O(n)   build the sorted array
        output[counts[num]-1] = num     #Time -> O(1)   Places the values in their correct position
        counts[num] -=1                 #Time -> O(1)   decrements the count by one and then repeats for the next value

    return output                       #Time -> O(1)   returns the final array
                                        #Total -> O(n+m)

#arr = [84,39,583,239,542,245,1,69]

size=int(input("Enter the size of the array: "))

arr=[]
for _ in range(size):
    value = int(input("Enter a Value: "))
    arr.append(value)

print("Unsorted array: ",arr)
sortedArr = countSort(arr)
print("Sorted array: ",sortedArr)
'''