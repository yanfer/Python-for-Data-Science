#Open
"""  
In this section we will use Python’s built-in open function to create a file object and obtain the data from a txt file.
We will use Python’s open function to get a file object. We can apply a method to that object to read data from the file.
"""
        #File Directory  #File Name
File1=open('Example.txt','r')
                                    #Mode

"""  
We can open the file Example1 ". txt" as follows We use the open function.
The first argument is the file path. This is made up of the file name and the file directory.
The second parameter is the mode; common values used include 'r' for reading, 'w' for writing and 'a' for appending. We will use ‘r’ for reading.
"""

print(File1.mode) # r

""" You should always close the file object using the method close. """
File1.close()

"""  
This may get tedious sometimes, so let’s use the “with statement.”
Using a 'with' statement to open the file is better practice because it automatically closes the file.
"""

with open("Example.txt","r") as File2:
    file_stuff=File2.read()  # The method read stores the values of the file in the variable file_stuff as a string.
    print(file_stuff)       #You can print the file content.
    
print(File2.closed) #You can check if the file content is closed, but you cannot read from it outside the indent.
print(file_stuff)#But you can print the file content outside the indent as well.
  
with open("Example.txt","r") as File3:
    file_lines=File3.readlines() #We can output every line as an element in a list using the method readlines.

with open("Example.txt","r") as File4:
    file_line=File4.readline() # If we run this command, it will store the first line in the variable file_stuff, then print the first line.



#WE CAN ONLY USE ONE METHOD EACH TIME


with open("Example.txt","r") as File5:
    for line in File5:  
        print(line)       #We can use a loop to print out each line individually as follows.


""" We can specify the number of characters we would like to read from a string as an argument to the method readlines. """

with open("Example.txt","r") as File6:
        file_readlines=File6.readlines(1)
        print(file_readlines) # When we use a 4 as an argument in the method readlines, we print out the first four characters in the file.
        file_readlines=File6.readlines(1) #If we call the method a second time, the next line is printed out.
        print(file_readlines)
        file_readlines=File6.readlines(1)
        print(file_readlines)



with open("Example.txt","r") as File7:
        i = 0
        for line in File7:
            print("Iteration", str(i), ": ", line)   #We can use a loop to iterate through each line
            i = i + 1
            

with open("Example.txt","r") as File8:
    FileasList = File8.readlines() #We can use the method readlines() to save the text file to a list

# Print the first line
print(FileasList[0] )

# Print the second line
print(FileasList[1] )