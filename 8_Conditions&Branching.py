#Comparison operations
""" 
Let's asign to "a" a value of 6
We can use the "==" operator to determine if two values are equal 
"""
a=6
print(a==7) #False

i=5
print(i>=5) #True

""" 
The inequality test uses an explanation mark "!" preceding the equal sign "=", if two operands are not equal,
then the condition becomes true.
"""

j=2
print(j!=6) #True

print("AC/DC"=="Michael Jackson") #False
print("AC/DC"!="Michael Jackson") #True

#Branching
""" 
Branching allow us to run different statements for different input.
It's helpful to think of an “if statement” as a locked room:
If the statement is true, you can enter the room, and your program can run some predefined
task.
If the statement is false, your program will skip the task.
"""

#the brackes for if are not necessary
age = 18
if age>=18:
    print("you can enter")
print("move on")

#else and if
age2 = 15
if age2>=18:
    print("you can enter")
else:
    print("go to see Meat Loaf")
print("move on")

#elif
age3 = 18
if age3>18:
    print("you can enter")
elif age3==18:
    print("go to see Pink Floyd")
else:
    print("go to see Meat Loaf")
print("move on")

#Logic Opreators
"""
Logic operations take Boolean values and produce different Boolean values.
"""
#not
"""
The first operation is the not operator.
If the input is true, the result is a false.
Similarly, if the input is false, the result is a true.
"""
print(not(False)) #True

#or
"""
The “or” operator takes in the two values, and produces a new Boolean value.
To be true just one condition should be true.
"""

album_year = 1990
if album_year < 1980 or album_year > 1989:
    print("The album was made in the 70's or 90's")
else:
    print("The album was made in the 80's")

#and
"""
The "and" operator takes in the two values, and produces a new Boolean value. 
To be true both conditions should be true.
"""

album_year2 = 1980
if album_year2 > 1979 or album_year2 < 1990:
    print("The album was made in the 80's")

