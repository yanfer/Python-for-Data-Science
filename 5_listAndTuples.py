#Tuples are an ordered sequence, written as coomma-separated elements within parentheses
Ratings=(10,6,12,7,5,9,2)

#There are different types, strings, integer and float, they can all be contained in a tuple but the type of the variable is tuple.
tuple1 = ('disco',10,1.2)

#they can be access via an index, using the name of the tuple followed by a square bracket with the index number
print(tuple1[0])
 
 #we can use negative index (-1 last item, -3 in this case first item)
print(tuple1[-3])

#We can concatenate or combine tuples by adding them
tuple2 = tuple1 + ('hard rock', 10)

print(tuple2)

#If we would like multiple elements from a tuple, we could also slice tuples
#if we want the first three elements we use:
print(tuple2[0:3])

#the last index (3) is larger than the index you want, similarly, if we want the last two elements we use the following command
print(tuple2[3:5])

#len command to obtain the length of a tuple.
print(len(('disco', 10, 1.2, 'hard rock', 10)))

#Tuples are immutable, we can't change them. Let's see why this is important.
Ratings1 = Ratings

#Ratings1[2] = 4            #TypeError: 'tuple' object does not support item assignment

Ratings = Ratings + (1,7)
print(Ratings) #(10, 6, 12, 7, 5, 9, 2, 1, 7)

#Ratings1 will not be affected by a change in Rating because the tuples are immutables.
print(Ratings1) #(10, 6, 12, 7, 5, 9, 2)

#We can assing a different tuple to a variable with a previous tuple
Ratings = (2,10,1,9,4)

print(Ratings)

#Because of  immutability, if we would like to manipulate a tuple, we must create a new tuple instead.
#for example if we would like to "sort" a tuple, we use the function sorted, the input is the original tuple, the output is a new sorted list.

RatingsSorted = sorted(Ratings)
print(RatingsSorted)
print(type(RatingsSorted))
print(type(Ratings))

#Nesting
#A touple can contain other touples as well as other complex data types. This is called nesting
#we can access to these elements using the standard indexing methods.
NT = (1,2,("pop","rock"),(3,4),("disco",(1,2)))
#     0,1,      2,         3,        4

print(NT[2][1])  #rock

#Lists

#Lists are also ordered sequences, a list s represented with square brackets [] and are MUTABLE
#We can also nest tuples and other data structures; the same indexing conventions apply for nesting.
L = ['Michael Jackson', 10.1, 1982, [1,2],('A',1)]
#          0             1       2    3      4
#         -5            -4      -3   -2     -1
#Like tuples each element of a list can be accessed via an index

#We can use slicing in lists.
print(L[3:5])

#We can concatenate or combine lists by adding them
L1 = ['Michael Jackson', 10.1, 1982]
L2 = L1 + ["pop",10]
print(L2)

#Lists are mutablel, therefore, we can change them, we can apply the method extends by adding a "dot" followed by the name of the method, then parenthesis
L.extend(["pop",10])
print(L)

#Another similar method is append, instead of a extended we add JUST ONE element to the list

L3 = ['Michael Jackson', 10.1, 1982]
L3.append(["pop", 10])
print(L3)

#['Michael Jackson', 10.1, 1982, ['pop', 10]]
#        0            1     2        3

#If we look at the index, there is only one more element, index 3 contains the list we appended.

#As list are mutable we can change them, we can change the first element as follows.
A = ["disco", 10, 1.2]
A[0]= "hard rock"
print(A) #['hard rock', 10, 1.2]

#We can delete an element using the "del" command, we simply indicate the list time we wuld like to remove as an argument
del(A[0])
print(A) #[10, 1.2]

#We can convert a string to a list using split, method split converts every group of characters separated by a space into an element of a list
print("hard rock".split()) #['hard', 'rock']

#We can use the split function to separate strings on a specific character, knows a delimiter. We simply pass the delimeter we would like to split on as an argument.
print("A,B,C,D".split(",")) #['A', 'B', 'C', 'D']

#the result is a list, each element correspond to a set of characters that have been separated by a comma.

#List: Aliasing
#When we set one variable, B equal to A, both A and B are referencing the same list. Multiple names referring to the same object is known as aliasing.
#If we change the first element in "A", we get a side effect; the value of B will change as a consequence.

A1 = ["disco", 10, 1.2]
B1 = A1 #["disco", 10, 1.2]

A1[0]= 'banana'
print(B1) #['banana', 10, 1.2]

#We can clone a list using the following syntax
A3 = ["disco", 10, 1.2]
B=A3[:]
print(B)

#In this case variable "B" referes a new copy or clone of the original list, now if I change "A", "B" will not change.
A3[0]= 'banana'
print(A3) #['banana', 10, 1.2]
print(B) #['disco', 10, 1.2]

#We can get more info on lists, tuples and many other objects in Python using the "help" command
#help(A3)

B4=["a","b","c"]
print(B4[1:])