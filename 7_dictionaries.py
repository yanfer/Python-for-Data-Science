#Dictionaries
"""
Dictionaries are a type of collection in Python, if we recall a list has integer indexes. These are like addresses.
A list also has elements. A dictionary has keys and values.
They key is analogous to the index, they are like addresses but they don't have to be integers. They are usually characters;
The values are similar to the elements in a list and contains information.
"""

#To create a dictionary we use curly brackets "{}"
#The keys have to be immutable and unique
#The values can be immutable, mutable and duplicates.
{"key1":1, "key2":"2","key3":[3,3,3],"key4":(4,4,4),"key5":5}

DICT = {"Thriller":1982, "Back in Black":1980, "The Bodyguard":1992}
#To find an item in a dictionary
print(DICT["Thriller"]) #1982

#To add an item in a dictionary
DICT["Graduation"]=2007

print(DICT) #{'Thriller': 1982, 'Back in Black': 1980, 'The Bodyguard': 1992, 'Graduation': 2007}

#To delete an entry key and value
del(DICT["Graduation"])
print(DICT) #{'Thriller': 1982, 'Back in Black': 1980, 'The Bodyguard': 1992}

#We can verify if an element is in the dictionary using the "in" command
print("The Bodyguard" in DICT) #True

print(DICT.keys()) #dict_keys(['Thriller', 'Back in Black', 'The Bodyguard'])
print(DICT.values()) #dict_values([1982, 1980, 1992])