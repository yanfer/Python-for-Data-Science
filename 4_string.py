Name =  "Michael Jackson"
print(Name)
#index:0-14

print(Name[0]) #M

print(Name[6]) #l

#We can aslo use negative index, the las element is -1
#in this case can be from -15 to -1
print(Name[-1]) #n

#We can think of string as a list or tuple and perform sequence operations
print(Name[0:4]) #Mich

#WE can also input a stride value. frist value is where we'll start (anything means 0 -> ::2) and the second every (2nd, 3rd, 4th...) value
print(Name[2::2]) #calJcsn   

#We can incorporate sling with stride too, in this case from 0 index to 5
print(Name[:5:2]) #Mca

# len to obtain the lenth of the string
print(len("Michael Jackson")) #15

#We can combine strings
Statement = Name + " is the best"
print(Statement) #"Michael Jackson is the best"

#We can replicate Values in a string simply multiply the string by the number
print(3*"Michael Jackson") #"Michael JacksonMichael JacksonMichael Jackson"

#We cannot change the value of the string in the case above but we can create a new string
Name = Name+" is the best"
print(Name)

#String are immutable, backslashes "\" represent the beginning of escape sequences
#Escape secuences represent strings that may be difficult to input
#\n is new line
print("Michael Jackson \nis the best")

#\t represent a tab
print("Michael Jackson \tis the best")

#if you want to use a backslash in you string use a double backslash
print("Michael Jackson \\ is the best")
#or we can place an r in front of the string
print(r"Michael Jackson \ is the best")

#We can apply methods to a string, when we apply a method to the string "A" we get a new string "B" that is different from "A"

#Method upper make the characters uppercase
A = "Thriller is the sixth studio album"
B=A.upper()
print(B) #"THRILLER IS THE SIXTH STUDIO ALBUM"

#Method replace replaces a segment of the string
C = "Michael Jackson is the best"
D= C.replace('Michael', 'Janet')
print(D) #"Janet Jackson is the best"

#Method find finds sub-strings
print(C.find('el')) #5  and its the frist index of the sequence

print(C.find('Jack')) #8

#if the sub-string is not inthe string, the output is negative one -1
print(C.find('(*D)')) #-1

Numbers = "0123456"
print(Numbers[::2])

print("0123456".find('1'))