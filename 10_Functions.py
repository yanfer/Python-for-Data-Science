#Functions
"""
Functions take some input then produce some output or change. The Function is just a piece of code you can reuse.
Python has many build-in functions.
"""

#Python functions
#Len
"""
len takes in an input of type sequence, such as a string or list, or type of collection, such as a dictionary or set, and returns the lenght of
that sequence or collection.
"""

album_ratings = [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5]

L = len(album_ratings)
print(L) # 8

#Sum
"""
The function sum takes in an iterable like a tuple or list and returns the total of all the elements.
"""

S=sum(album_ratings)
print(S) # 70.0

#Sorted vs Sort
""" 
There are two ways to sort a list. The first is using the function sorted.
We can also use the list method sort. Methods are similar to functions.
The function sorted Returns a new sorted list or tuple.
"""
sorted_album_rating=sorted(album_ratings)
print(sorted_album_rating) #[7.0, 7.0, 8.5, 9.0, 9.5, 9.5, 9.5, 10.0]

""" 
If we look at the list album ratings, nothing has changed. 
If we use the method sort, the list album ratings will change and no new list will be created.
"""

album_ratings.sort()
print(album_ratings) # [7.0, 7.0, 8.5, 9.0, 9.5, 9.5, 9.5, 10.0]

""" Unlike the previous case, we see that the list album rating has changed. In this case, no new list is created. """

#Making functions
""" To define a function, we start with the keyword "def". The name of the function should be descriptive of what it does. """

def add1(a):
    b=a+1
    return b

print(add1(5)) # 6

c = add1(10)
print(c) # 11

#Multiple Parameters
"""  
A function can have multiple parameters. 
The function "mult" multiplies two numbers; in other words, it finds their product.
If we pass the integers 2 and 3, the result is a new integer. 
"""

def Mult(a,b):
    c=a*b
    return c
print(Mult(2,3)) #6


""" If we pass the integer 10 and the float 3.14, the result is a float 31.4. """ 
print(Mult(10,3.14)) #31.400000000000002

"""
If we pass in the integer two and the string “Michael Jackson,” the string Michael Jackson is repeated two times. 
This is because the multiplication symbol can also mean repeat a sequence.
""" 
print(Mult(2,"Michael Jackson")) # Michael JacksonMichael Jackson

"""
If you accidentally multiply an integer and a String instead of two integers, you won’t get an error.
Instead, you will get a String, and your program will progress, potentially failing later because you have a String where you expected an integer.
"""

#No return functions
""" 
In many cases a function does not have a return statement. In these cases, Python will return the special “None” object. 
Practically speaking, if your function has no return statement, you can treat it as if the function returns nothing at all.
"""
def MJ():  
    print("Michael Jackson")

MJ() #Michael Jackson

""" 
Let's define the function “No work” that performs no task. Python doesn’t allow a function to have an empty body, 
so we can use the keyword pass,which doesn’t do anything, but satisfies the requirement of a non-empty body. 
"""
def NoWork():
    pass
print(NoWork()) # None

""" 
If we call the function and print it out, the function returns a None.
In the background, if the return statement is not called, Python will automatically return a None. 
"""

#Multitask Functions
""" Usually, functions perform more than one task. """

def moreAdd(a):
    b=a+1
    print(a, " plus 1 equals: ",b)
    return b
moreAdd(6) # 6  plus 1 equals:  7


#Loops in functions
""" We can use loops in functions.  """
def printStuff(Stuff):
    for index, value in enumerate(Stuff):
        print("Album ", index, "Rating is ", value)

album_ratings2 = [10.0,8.5,9.5]
printStuff(album_ratings2)
""" 
Album  0 Rating is  10.0
Album  1 Rating is  8.5
Album  2 Rating is  9.5
"""

#Variadic Parameters (*)
""" Variadic parameters allow us to input a variable number of elements. The function has an asterisk on the parameter names.
When we call the function, we call the parameters packed into the tuple. We then iterate through the loop; the values are printed out accordingly."""

def ArtistNames (*names):
    for name in names:
        print(name)

ArtistNames("Michael Jackson", "AC/DC", "Pink Floyd") #Michael Jackson AC/DC Pink Floyd

#Scope
""" The scope of a variable is the part of the program where that variable is accessible. Variables that are defined outside of any
function are said to be within the global scope, meaning they can be accessed anywhere after they are defined. """

""" Here we have a function that adds the string DC to the parameter y. """
def AddDC(y):
    y=y+"DC"
    print(y)
    return(y)

""" When we reach the part where the value of x is set to AC, this is within the global scope, meaning x is accessible anywhere after it is defined. """

x="AC"

""" A variable defined in the global scope is called a global variable. When we call the function, we enter a new scope or the scope of AddDC. """
z=AddDC(x) # ACDC

""" The function returns the value and is assigned to z. Within the global scope, the value z is set to ACDC. 
After the value is returned, the scope ofthe function is deleted. """

#Scope: Local Variables
""" Local variables only exist within the scope of a function. When we call the function, we create a new scope."""

def Thriller():
    Date = 1982 #The value of date doesn't exist within the global scope
    return Date

print(Thriller()) # 1982

""" Variables inside the global scope can have the same name as variables in the local scope with no conflict. """
Date = 2025
print(Date) # 2025

""" If a variable is not defined within a function, Python will check the global scope. """
def ACDC(y):
    x=Rating + y
    print(x)
    return (x)

Rating = 9
""" The value of z in the global scope will be 10, as we added one. """
Z=ACDC(1) #10
""" The value of rating will be unchanged within the global scope. """
print(Rating) #9

def PinkFloyd():
    global ClaimedSales #If we define the variable Claimed Sales with the keyword global, the variable will be a global variable.
    ClaimedSales = "45 million" 
    return ClaimedSales

PinkFloyd()
print(ClaimedSales)

def f(*x):
    return sum(x)

print(f())