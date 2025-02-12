# Import the library
#Now we are going to create a class Circle, but first, we are going to import a library to draw the objects:
import matplotlib.pyplot as plt

""" Python has a lot of data types """
#Types:
""" 
int: 1,546,856
float: 1.5, 58.78
String: "a", "abc"
list:[1,2,"abc"]
Dictionary: {"dog":1, "Cat": 2}
Boolean: False, True
"""
""" Each is an object """

#Objects
""" 
Every object has the following: 
*A type, 
*An internal data representation (a blueprint), 
*A set of procedures or functions called methods to interact with the data. 
"""

#Objects: Type
""" An object is an instance of a particular type.
Let’s do several less abstract examples. Every time we create an Integer, we are creating an instance of type integer, or we are creating an integer object.

In this case, we are creating five instances of type integer or five integer objects.
"""

""" Instance of type int """
Object1: 1
""" Instance of type int """
Object2: 12
""" Instance of type int """
Object3: 391
""" Instance of type int """
Object4: 78
""" Instance of type int """
Object5: 32

""" We can find out the type of an object by using the type command.  """
print(type([1,25,36])) #<class 'list'>

print(type(1)) #<class 'int'>

print(type("The cat is yellow")) #<class 'str'>

print(type({"dog":1, "cat":2})) #<class 'dict'>

#Methods
""" A class or type’s methods are functions that every instance of that class or type provides. It’s how you interact with the object. 

Consider the list Ratings. The data is a series of numbers contained within the list. The method sort will change the data within the object.
We call the method by adding a period at the end of the object’s name and the method’s name we would like to call with parenthesis.
"""
Ratings= [10,9,6,5,10,8,9,6,2]
Ratings.sort()
print(Ratings) #[2, 5, 6, 6, 8, 9, 9, 10, 10]

""" We can call the reverse method on the list, changing the list again. We call the method, reversing the order of the sequence within the object. """
Ratings.reverse()
print(Ratings) #[10, 10, 9, 9, 8, 6, 6, 5, 2]

#Creating Your Own Types: Defining Classes
#Classes
""" 
The class has data attributes. The class has methods. We then create an instance or instances of that class or objects.
The class data attributes define the class.

Let's create two classes; the first class will be a circle, the second will be a rectangle. Let's think about what constitutes a circle.
Examining this image all we need is a radius to define a circle and let's add color to make it easier to distinguish between different instances 
of the class later. Therefore, our class data attributes are radius and color.
Similarly, examining the image in order to define a rectangle, we need the height and width.
"""

"""
To create a class, you will need to include the class definition. This tells Python you are creating your own class.  
For this course in parenthesis, you will always place the term object. This is the parent of the class.
"""

                    #Name of the class
"""  class           Circle              (object): """ #<--Class parent 
    #Class Definition

""" Classes are outlines we have to set the attributes to create objects. """

""" 
Classes are outlines we have to set the attributes to create objects.
We define our class. We then initialize each instance of the class with data attributes radius and color using the class constructor.
The function "in-it" is a constructor. It’s a special function that tells Python you are making a new class, it's used to initialize data attributes. 
"""

""" 
The ‘radius’ and ‘color’ parameters inside __init__ are used to initialize the radius and color data attributes of the class instance.

The ’self’ parameter refers to the newly created instance of the class.

The parameters ’radius’ and ’color’ can be used in the constructor’s body to access the values passed to the class constructor 
when the class is constructed. """

class Circle (object):  # <--- Define your class    
    def __init__(self, radius, color):     # <--- Data attributes used to
        self.radius = radius               # <--- initialize each instance
        self.color = color                 # <--- of the class


""" 
After we have created the class, in order to create an object of class circle, we introduce a variable; this will be the name of the object. 
We create the object by using the object constructor.
"""
#Object name       #Data attributes
C1 = Circle(10,"red")        
            #Object constructor

""" 
It is helpful to think of self as a box that contains all the data attributes of the object. 
Typing the object's name followed by a dot and the data attribute name gives us the data attribute value, for example radius. In this case, the radius is ten.
"""
print(C1.radius) #10

""" 
In Python, we can also set or change the data attribute directly. Typing the object's name, followed by a dot
and the data attribute name, and set it equal to the corresponding value. 
"""
C1.color = "blue"
print(C1.color) #blue

""" Usually, in order to change the data in an object we define methods in the class. """

#Methods

""" 
We have seen how data attributes consist of the data defining the objects. 
Methods are functions that interact and change the data attributes, changing or using the data attributes of the object. 
"""
""" 
Let's say we would like to change the size of a circle; this involves changing the radius attribute. We add a method "add radius" to the class Circle.
he method is a function that requires the
self as well as other parameters. In this case, we are going to add a value to the radius;
"""

class Circle2 (object):  # <--- Define your class    
    def __init__(self, radius, color):
        self.radius = radius   
        self.color = color 

    def add_radius(self, value):   
        self.radius = self.radius + value        # <--- Method used to add "value" to radius

"""  
We call the method by adding a dot followed by the method name and parenthesis. 
In this case, the argument of the function is the amount we would like to add. 
We do not need to worry about the self-parameter when calling the method—just like with the constructor, Python will take care of that for us. 
In many cases, there may not be any parameters (other than self) specified in the method’s definition, so we don’t pass any arguments when calling the function. 
"""

C2 = Circle2 (2, "red")
C2.add_radius(8)
print(C2.radius) #10


""" We can add default values to the parameters of a class’s constructor. """
class Circle3 (object):  
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

""" 
The “D I R” function is useful for obtaining the list of data attributes and methods associated with a class. 
The object you’re interested in is passed as an argument. The return value is a list of that object’s data attributes. 
(The attributes surrounded by underscores are for Internal Use and you shouldn’t have to worry about them.)

The regular-looking attributes are the ones you should concern yourself with, these are the object’s methods and data attributes.
"""

print(dir (Circle3))