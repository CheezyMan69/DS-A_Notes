#Notes -----------------------------------------------------------------------------
'''
Algorithms Introduction
    Algorithms are very important in CS due to it being the main thing for computing.
    It can be found in many things like websites, games, softwares, etc.
    They take an input, run it through a way of solving it, and gives us an output.
    The bigger the input, the algorithm will take longer time to form an output
   
    There are 2 aspects of Algorithms:
        - Time complexity = How much time it takes to run.
                            Can be calculated practically by importing time to python but normally
                            we use theoretical analysis to evaluate the speed without any influence of
                            hardware or software using pseudocode and the n for input size. Taking the worst case
                            scenario (longest time possible) is required.

                            Examples of things taking time:
                                - assigning (=) = 1 unit of time (uT)
                                - +-*/ take 1uT
                                - print() = 1uT
                                - func() = 1uT
                                - Arrays = 1uT
                                - return = 1uT
                            
                            Using this knowledge we can run a code and calculate how much time it would take (theoretically):
                                x=10        1uT
                                y=20        1uT
                                z=x+y       2uT (= and +)
                                print(z)    1uT
                            ---- Total = 1+1+2+1 = 5uT ----

                            for loops take as long as they need to check for each value
                            Example of for loop:

                                num = 10;    1uT

                                for(i=1;i<=num;i++){
                                    print(i);            this for loop takes 11uT (assigns then checks then prints then adds then repeats until i>num)
                                }
                            ---- Total = 1+11 = 12uT ----
                            This previous example can change due to num being different (like num = 20)
                            so it can be calculated this way
                            1+1+n+1+1+n = {2n+4} (creates a function that we can use to calculate the worst case scenario)

                            Another Example:
                                int sumOfN (num){       1uT
                                    total = 0;          1uT
                                    for (i=0;i<=num;i++){   1+n+1+n
                                        total = total + i;  2xn
                                    }
                                    return total;       1uT
                                }
                            ---- Total = 1+1+1+n+1+n+2xn+1 = 4n+4 uT ----
                            
                            More fucking examples:
                                func sumInteger (n):
                                    sum = 0;            1uT
                                    for(i=1;i<=n;i++){  1+(n+1)+n uT
                                        sum = sum + i;   n+n uT (keeps occurring due to loop)
                                    }
                                    return sum;         1uT

                                func Main{
                                    x = 5;              1uT
                                    print(sumInteger(x)); 2uT
                                }
                            ---- Total = (1+(1+(n+1)+n)+(n+n)+1)+1+2 = 4n+6 uT ----

                            EVEN MORE EXAMPLES FOR FUCK SAKE: #how many more fucking examples im sick of this :[
                                func maxArray(amm){
                                    max = amm[0];       2 uT                
                                    n = len(amm);       2 uT
                                    for(i=1;i<n;i++){   1+(n)+n uT (due to i<n it will only check n times unlike i<=n where it checks an extra time)
                                        if(max<amm[i]){ n+n uT
                                            max = amm[i];   n+n uT
                                        }
                                    }
                                    return max;         1 uT
                                }
                            ---- Total = 2+2+(1+n+n)+2n+2n+1 = 6n+6 uT ----

                            After we estimate the running time for the function, we can calculate the Growth Rate of it
                            this is is taken by finding the fastest and slowest times
                            a = fastest
                            b = slowest
                            a(6n+6)<=T(n)<=b(6n+6) (example)
                            T(n) is the Growth rate
                            No matter the change in environment (software or hardware) it will only affect the growth
                            at a constant rate (the Growth rate is bound by 2 linear functions)

                            The growth rate can be any of the 7 functions:
                                - Constant = 1
                                - Logarithmic = log n
                                - N-log-N = n log n
                                - Quadratic = n^2
                                - Cubic = n^3
                                - Exponential = 2^n
                            
                            This is a result of how much space the algorithm would take. The more space, the more time
                            but that also depends on what the algorithm does.

                            One of the ways to calculate the growth rate, we can use the Big-O notation:
                                This is done by ignoring all constants in the function and focusing on the highest degree of n because
                                that is the biggest value in the function so we can use it to calculate the worst case scenario.

                                O(g(n)) = f(n)<=cg(n)       c = constant
                                    for n = n0
                                if there is only constant it will be O(1) always no matter how big the constant is

                                Examples:
                                    f(n)= 7n-2                              O(f(n)) = O(n)
                                    f(n)= 10n^3 + 20n^2 +100n+100000000     O(f(n)) = O(n^3)
                                    f(n)= 6log(n)+9494                      O(f(n)) = O(log(n))
                            
                            Big-O rules:
                                - Only use the highest degrees of the dominant term (n)
                                - ignore the constants
                                - ignore the lower degrees
                                - used only for worst case scenarios

                            Computing Prefix Averages:
                                This is an algorithm that calculates the average of an inputted array by adding the previous value
                                and dividing by n (which is the amount of values so far) and it repeats until the end of the array
                                (example in the #Code below)
                                Through these 2 examples (quad and linear) we can see that the linear variant will take less time
                                due to the lower degree. As the n grows the time will always be lower than n^2 in the quad variant.
                            
                            Big-O is used for the worst case scenario, but what if you want to calculate the best case or the average case?
                            The answer is to use the Big-Omega notation (best case) or the Big-Theta notation (average case).
                                Big-Omega Rules:
                                    - Only use the lowest degrees of the dominant term (n)
                                    - Ignore the constants
                                    - Ignore the highest degrees
                                    - Used only for best case scenarios
                                Example of Big-Omega:
                                    6n^2+5n+13 uT -> O(n)
                                
                                Big-Theta Rules:
                                    - Only use the dominant term (n)
                                    - Ignore the constants
                                    - Used for an average case
                                Example of Big-Theta:
                                    6n^2+5n+13 uT -> O(n^2 + n)                               

        - Space complexity = How much space does the algorithm take
                             This uses 2 types, Auxiliary and Total
                                - Auxiliary calculates the space needed without any input. This includes:
                                    + Variables
                                    + Data Structures
                                    + Any additional memory needed

                                - Total calculates all the space including input. This includes:
                                    + Auxiliary space
                                    + Input
                             
                             To calculate the Space complexity you need to do the following:
                                - Identify Variables and Data Structures
                                - Analyze memory consumption
                                - Ignore constants (Big-_ notation)
                                Examples in code below (in unit space [uS])

'''
#Code ------------------------------------------------------------------------------
#Time Complexity -------------------
'''
#Computing Prefix Averages (Quad)---
def prefixAverage(x):
    n= len(x)                       #1+1 uT -> O(1)
    A = [0]*n                       #1+1*n -> O(n)
    
    for i in range(n):              #for(i=0; i<n;i++) 1+n+n uT -> O(n)
        total = 0                   #1 uT -> O(1)
        for j in range(i+1):        #for(j=0;j<i+1;j++) 1+n+n uT -> O(n) (j loop is dependant on the i loop so in the total they are multiplied)
            total +=x[j]            #1+1+1 uT -> O(1)
        
        A[i] =total/(i+1)           #1+1+1 uT -> O(1)
    return A                        #1 uT -> O(1)
                                    
                                    #Total of function  = O(1)+O(n)+[O(n)*O(1)*O(n)*O(1)*O(1)]+O(1)
                                    #                   = O(1)+O(n) + O(n^2) + O(1)
                                    #                   = O(n^2) (because we only take the highest degree)

X = [1,2,3,4,5]
print("A ->",prefixAverage(X))
'''
'''
#Prefix Averages (Linear) ----------
def prefixAverageLin(X):            
    n=len(X)                        #1+1 uT -> O(1)      
    A=[0]*n                         #1+n uT -> O(n)

    total= 0                        #1 uT   -> O(1)
    for i in range(n):              #for(i=0;i<n;i++) -> 1+n+n uT -> O(n)
        total+=X[i]                 #1+1+1 uT -> O(1)
        A[i] = total / (i+1)        #1+1+1+1 uT -> O(1)

    return A                        #1 uT -> O(1)
                                    #Total of Function  = O(1)+O(n)+O(1)+[O(n)*O(1)*O(1)]+O(1)
                                    #                   = O(1)+O(n)+O(1)+ O(n) + O(1)
                                    #                   = O(n) 

X=[1,2,3,4,5]
print("A->", prefixAverageLin(X))
'''
#Space Complexity ------------------
'''
#Find Max --------------------------
def findMax(arr):
    maxElement = arr[0]             #1 uS -> O(1)   (creating variable maxElement)
    for num in arr:                 #1 uS -> O(1)   (creating variable i)
        if num>maxElement:
            maxElement=num
    return maxElement               #Total space = 1+1 uS = O(1)
'''
'''
#Fibonacci -------------------------
def fibonacci(n):
    fib = [0] *(n+1)                #n uS (creating an array of size n)
    fib[1]=1                        

    for i in range(2,n+1):          #1 uS (creating variable i)
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]                   #Total = 1+n = O(n)
'''
#Calculating both Complexities -----
'''
#3D sum ----------------------------
def threeDSum(arr):
    total = 0                           #Time = 1uT -> O(1)                         Space = 1uS -> O(1)
    n = len(arr)                        #Time = 1uT -> O(1) (calling len)           Space = 1uS -> O(1) (creating n)

    for i in range (n):                 #Time = for(i=0;i<n;i++)= 1+n+n uT = O(n)   Space = 1uS -> O(1) (creating i)
        for j in range(n):              #Time = for(j=0;j<n;j++)= 1+n+n uT = O(n)   Space = 1uS -> O(1) (creating j)
            for k in range(n):          #Time = for(k=0;k<n;k++)= 1+n+n uT = O(n)   Space = 1uS -> O(1) (Creating k)
                total +=arr[i][j][k]    #Time = O(1)

    return total                        #Time = 1uT = O(1)
                                        #Total Time = O(1)+O(1)+[O(n)*O(n)*O(n)*O(1)]+O(1)
                                        #           = O(n^3)
                                        #Total Space = O(1)+O(1)+O(1)+O(1)+O(1)
                                        #           = O(1)
'''
'''
#Lin search ------------------------
def linSearch(arr,target):
    for num in arr:                 #Time = O(n)            Space = O(1) (creating num)
        if num == target:           #Time = O(1) (checking)
            return True             #Time = O(1)
    return False                    #Time = O(1)
                                    #Total -> Time = O(n)   Space = O(1)
'''