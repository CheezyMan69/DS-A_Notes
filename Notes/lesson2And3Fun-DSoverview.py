#Notes -----------------------------------------------------------------------------
'''
Linear Data Structures - 
    - Arrays = Fixed Size

    - Dynamic Arrays = resizable (called Lists in Python)

    - Pointers = var that store memory addresses, security issue cuz of memory access, can change values indirectly
                    Not used in high level prog languages (in C and C++ but not Python or C#) 
                        in Python -> use refrences instead of Pointers (A=[1,2,3,4] -> ref is A[4]=10)
    
    - Linked Lists (LL) = resizable, uses memory allocation to link values with one another
                            stores a value and a memory address -> the memory address is for the next value in line (Pointer)
                                This is used to get things that are far apart from one another unlike an array where they are all next to
                                one another in the memory 
    
    - Doubly Linked Lists (DLL) = similar to Linked Lists but instead of only a next memory address it also houses a previous memory address
                                    This allows it to go back and forth (Backwards to the previous address and Forwards to the next address)
                                         Sorting in this way is much much faster (apperantly)
                                             For LL it only goes one way so more itterations for sorting but for DLL it can go back and forth so the 
                                             amount of itterations are less getting it to sort faster
                                                LL can take up to 6 itteration for sorting one list but DLL can do it in 3 itterations for the same list
'''
'''
Data Structures in Python -
    - Lists = changable (mutable), uses [], (Dynamic Arrays)
    - Tuples = cannot be changed later on (immutable), uses (), for fixed values (use when you dont want to change data again)
    - Dictionaries = uses a key, contains any data type, changable (mutable), uses{}
    - Sets = size is mutable but elements are immutable, uses {}, fixed values but growing size
    - Arrays
'''
'''
#Lists -----------------------------
numbers = [1,2,3,4,5]                    
names = ["john","bob","kissma nuts"]
student = [1,"kissma nuts",True]        #lists can store multiple data types

for num in numbers:
    print(num)                          #procceds to type all the (num)bers in the list

for i in student:
    print(i)                            #prints out all the values in the list

student = [2,"ben dover",False]

for i in student:
    print(i)                            #prints the new list in student
'''
'''
#Tuples ----------------------------
point = (10,20)
dimensions = (100,200,50)
print(point)
print(point[0],"and",point[1])

for i in dimensions:
    print(i)
'''
'''
#Dictionaries ----------------------
person = {"firstName": "Ben", "lastName": "Dover", "age": 69,}          #firstName is the key and Ben is the value -> to access Ben you need to use firstName
                                                                        #keeps thing organized (the , keeps the keys seperated), it can be in a row or column

racer = {"name": "Carlos Sainz",
         "age": 29,
         "brand": "Ferrari",
         "gonnaLoseJob": True,
         "winningNow?": True}

print("My name is",person["firstName"],person["lastName"],"I am", person["age"],"years old")

print("Dictionary ->", person)

for key in racer:
    print(key,"->",racer[key])
'''
'''
#Sets ------------------------------
uniqueIds = {84857,848484,929292}

for num in uniqueIds:
    print(num)

#uniqueIds[0] = 11111   gives error that you can not change items

print("ids ->", uniqueIds)
'''
'''
import numpy as np   #pip instal numpy (numpy is a library that makes it easier to use numbers like arrays and matrices)

numbersArray = np.array([1,2,3,4,5,6,7])

print(numbersArray)

for num in numbersArray:
    print(num)
'''
#Examples --------------------------------------------------------------------------
'''
#List Example ----------------------
size = int(input("Enter the size of the list: "))
print("size of the list now is",size)

dataList = []                       #sets an empty list

print("enter the values for the list:")
for _ in range(size):               # _ is a place holder because we dont need a variable there (tells the loop to run until size is reached)
    value = input()
    dataList.append(value)          #append places the values into the list
print("List of data ->",dataList)
'''
'''
#Tuples Example --------------------
size = int(input("Enter the size: "))

dataTuple= tuple()
for _ in range(size):
    value = input()
    dataTuple +=(value,)            #For tuples to add values into it you need +=

print("Tuple ->", dataTuple)
'''
''''
#Dictionary Example ----------------
size = int(input("Enter the size: "))
dataDick = {}                       #sets an empty dictionary

print("Enter key value pairs: ")

for _ in range(size):
    key = input("Key name: ")
    if key == 'age':
        value = int(input("Enter age: "))
    else:
        value = input("Value for respective Key: ")

    dataDick[key] = value           #tells the program "for this key add this value"  

print("Dictionary -> ", dataDick)
for key in dataDick:
    print(key, "->",dataDick[key])
'''
'''
#Sets Example ----------------------
size = int(input("Enter the size: "))

dataSet = set()

for _ in range(size):
    value = input()
    dataSet.add(value)              #to add values you need to sets, use .add

print("Data Set ->", dataSet)
'''
'''
#Array using NumPy
import numpy as np
size = int(input("Enter the size: "))
dataArray = np.array([])

print("Enter NumPy Array Values")

for _ in range(size):
    value = input("enter value: ")
    dataArray= np.append(dataArray, value)  #use append to add values

print("NumPy Array ->", dataArray)
'''
'''
#List and Dicktionary combooo ------

size = int(input("Enter the size population: "))

population = []

for i in range(1,size+1):
    print("Enter details for person",i,": ")
    name = input("enter name: ")
    age = int(input("enter age: "))
    person={"name": name,
            "age": age}
    population.append(person)       #basically makes a list of dictionaries 

print("Population of city ->",population)

for person in population:
    print("Name: ", person["name"])
    print("Age:", person["age"])
'''
#study classes and objects----------------------------------------------------------
#HOMEWORK ON TEAMS FUN DUE BY SUNDAY (28 April 2024)--------------------------------