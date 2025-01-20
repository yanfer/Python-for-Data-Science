#Sets
#Sets are a type of collection. This means that like lists and tuples, you can input different python types. 
# Unlike lists and tuples they are unordered. This means sets do not record element position. 
# Sets only have unique elements. This means there is only one of a particular element in a set.

#To define a set, you use curly brackets You place the elements of a set within the curly brackets. 
Set1={'pop','rock','soul','hard rock','rock','R&B','rock','disco'}

#You notice there are duplicate items.When the actual set is created, duplicate items will not be present. 
# You can convert a list to a set by using the function set; this is called type-casting. You simply use the list as the input to the function set.
album_list = ['Michael Jackson', 'Thriller', 'Thriller',1982]
album_set = set(album_list)
print(album_set) # {'Thriller', 'Michael Jackson', 1982}

#The result will be a list converted to a set. The function set returns a set. Notice how there are no duplicate elements.


#Set Operations---------------------------------------------------------------

A = {"Thriller", "Back in Black", "AC/DC"}

#We can add an item to a set using the add method.

A.add("NSYNC")
print(A) #{'AC/DC', 'Back in Black', 'Thriller', 'NSYNC'}

#if we add the same item twice nothing will happen as there can be no duplicates in a set
A.add("NSYNC")
print(A) #{'AC/DC', 'Back in Black', 'Thriller', 'NSYNC'}

#We can also remove an item from a set using the remove method.
A.remove("NSYNC")
print(A)

#we can verify if an element is in the set using the "in" command.
print("AC/DC" in A) #True or False


#Mathematical set operations--------------------------------------------------
album_set_1 = {"AC/DC", "Back in Black","Thriller"}
album_set_2 = {"AC/DC", "Back in Black","The Dark Side of the Moon"}

"""
The intersection of two sets is a new set containing elements which are in both of those sets.
We can combine two sets and we can define the intersection in terms of "and".
In Python we use the ampersand "&" to find union of two sets.
"""
#After applying the intersection operation, all the items that are not in both sets disappear.

album_set_3 = album_set_1 & album_set_2
print(album_set_3) #{'AC/DC', 'Back in Black'}

#The "union" method unite the 2 sets of elements which contain all the items in both sets.
print(album_set_1.union(album_set_2))

""" 
The Album set 3 contains elements of album set 1 and 2, so its a subset, we can check if a set is a subset using the is subset method.
"""
print(album_set_3.issubset(album_set_1))

S={'A','B','C'}

U={'A','Z','C'}

print(U.union(S))