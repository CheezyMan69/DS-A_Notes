#this is gonna be fun

'''
#Print and Data Types---------------------
print("\t\thello world")
print("you learning python now?")
print("\tcongrats i guess, more work but sure\nwelcome to the 2nd sem boss\n\t\t\tENJOY\n")
x=10.2
y=20
print("x ->",x,"\ny->",y)
print("type of x ->",type(x))
print("Type of y ->",type(y))
sum=x+y
print("the sum of x and y ->",sum,"\nand its type ->",type(sum)) 

name="boss"
print("\nWatsup ",name,"\n'what type of name is that ->",type(name))
is_Boss=True
print("you the boss?",is_Boss,"\nWhat type of answer is that ->",type(is_Boss),"\n")
'''
'''
#Operators---------------------------------
a=10
b=20
print("a is",a,"\nb is",b,"\n")
print("Addition ->",a+b)
print("Subtraction ->",a-b)
print("Multiplication ->",a*b)
print("Division ->",a/b,"\n")

print("is a>b ->",a>b)
print("is a<b ->",a<b)
print("is a equal to b ->",a==b,"\n\n")

T=True
F=False
print("T is",T,"\nF is",F,"\n")
print("AND ->", T and F)
print("OR ->",T or F)
print("NOT ->",not T,"\n\n")
'''
'''
#If Statments--------------------------------
x=11
y=10

if x>y:
    print("\nx is greater that y")
elif x==y:
    print("\nwooooow you achived equality")
else:
    print("\nhow dare you make y greater than x\nyou monster")
print("x ->",x,"y ->",y,"\n")

print("enter your age:")   #also in input downstairs
age= int(input())    
if age==18:
    print("welcome to adulthood TAX TIME\n")
elif age>18:
    print("you have been an adult for a while\nhow does it feel?\n")
else:
    print("go away child, you are still too young for this world\ngo enjoy your childhood\n")
'''
'''
#While Loops-----------------------------------
count=0
while count<=5:
    print("Count: ",count)
    count+=1
'''
'''
#For Loops-------------------------------------
for i in range(2,5):
    print("No. of Iteration =",i)
print("\n")
'''
'''
#Functions-------------------------------------
#Defining Functions
def lol():       #function is called lol
    print("wasuuuuuuuuuuuuuuuup")
    print("whats your name?")
    name=input()
    print("nice to meet you",name,"\n")
#Calling Function
lol()

#Parameters and Functions
def add_for_some_reason(x,y):
    sum = x+y
    return sum

a = 10
b = 20
result =add_for_some_reason(a,b)
print("a is",a,"\nb is",b,"\nthe result of adding them is",result,"\n")
'''
'''
#Input(kinda skipped ahead but its fine)---------
name = input("Enter your name plz:")
print("are you sure your name is",name,"?\n(Y or N)\n")
confirmation = input()
if confirmation =="y" or confirmation == "Y":
    print("well done on being sure\n")
elif confirmation =="n" or confirmation == "N":
    print("how you not sure?\nwhats wrong with you\n")
else:
    print("why you give me bs? wasting my time\n")

print("enter your age now",name)
age= int(input())    
if age==18:
    print("welcome to adulthood",name, "ITS TAX TIME\n")
elif age>18:
    print("you have been an adult for a while",name,"\nhow does it feel?\n")
else:
    print("go away child, you are still too young for this world\ngo enjoy your childhood\n")
'''
