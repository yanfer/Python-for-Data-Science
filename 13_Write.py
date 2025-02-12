""" 
We can also write to files using the open function.
We will use Python’s open function to get a file object, to create a text file, we can
apply method write to write data to that file. As a result, text will be written to the file. 
"""

with open("Example2.txt","w") as File1: # "w" will create a new file called Example2
        File1.write("This is line A\n")
        File1.write("This is line B\n")
        
""" We can write each element in a list to a file. """

Lines=["This is line C\n","This is line D\n","This is line E\n"]

with open("Example2.txt","a") as File2:  # "a" will not create a new file instead will write below the last content in this file
    for line in Lines:
        File2.write(line)

""" We can copy one file to a new file """

with open("Example2.txt","r") as readfile:
    with open("Example3.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)
            
""" You can check the file to see if your results are correct. """

with open("Example3.txt", 'r') as testwritefile:
    print(testwritefile.read())
    
#Additional modes
# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.