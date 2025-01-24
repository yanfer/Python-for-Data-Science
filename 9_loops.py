# Loops
""" 
Before we talk about loops, let’s go over the range function.
The range function outputs an ordered sequence as a list “i”.
If the input is a positive integer, the output is a sequence; the sequence contains the same number of elements as the input, but starts at zero.
"""

""" For example, if the input is 3 the output is the sequence 0,1,2. """
print(range(3))

""" 
If the range function has two inputs where the first input is larger than the second input, the output is a sequence that starts at the first input.
Then the sequence iterates up to, but not including the second number.
"""
print(range(10,15)) #[10,11,12,13,14]

""" 
From Python 3 the range doesn't show explicitly like this [10,11,12,13,14] but range(10, 15)
"""

#for loops
""" 
We will focus on lists, but many of the procedures can be used on tuples. Loops perform a task over and over.
"""

squares=["red","yellow","green","purple","blue"]

for i in range(0,5):
    squares[i]="white"

print(squares) #['white', 'white', 'white', 'white', 'white']

""" 
We can also iterate through a list or tuple directly in Python, we do not even need to use indexes. 
"""
squares2=["red","yellow","green","purple","blue"]

for i, square2 in enumerate(squares2):
    square2
    i
    print(i) #0,1,2,3,4

#While loops
""" 
“While loops” are similar to “for loops”, but instead of executing a statement a set number of times, a while loop will only run if a condition is met.
"""

squares3 = ["orange","orange","purple","orange","blue"]
Newsquares = []
i=0

while(squares3[i]=="orange"):
    Newsquares.append(squares3[i])
    i=i+1

print(Newsquares) #['orange', 'orange']

A=[3,4,5]

for a in A:
    print(a)

    x=3

y=1

while(y!=x):
    print(y)
    y=y+1