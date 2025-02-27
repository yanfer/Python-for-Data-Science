""" We will be covering Numpy in 1D, in particular "n d arrays". Numpy is a library for scientific computing. 
It has many useful functions. There are many other advantages like speed an memory. Numpy is also the basis for pandas.
We will be covering: 
1) The Basics and Array Creation 
2) Indexing andSlicing 
3) Basic Operations 
4) Universal Functions"""

import numpy as np
"""  We can cast a list to a numpy array by first importing numpy.  """

print(np.__version__) #To check the numpy version


a=["0",1,"Two","3",4] #A Python list is a container that allows you to store and access data. Each element is associated with an index.
#   0  1   2    3  4

b=np.array([0,1,2,3,4]) # A "numpy" array or "ndarray" is similar to a list. It's usually fixed in size and each element is of the same type, in this case, integers.
""" We can access the data via an index.
As with a list, we can access each element with an integer and a square bracket."""

"""  If we check the type of the array we get "numpy.ndarray". """
print(type(b)) #'numpy.ndarray'

""" As numpy arrays contain data of the same type, we can use the attribute "dtype" to obtain the data type of the array’s elements. """

print(b.dtype) #int64


#ATTRIBUTES
#size
""" Let's review some basic array attributes using the array 'a'. 

The attribute 'size' is the number of elements in the array.  """

print(b.size) #5

"""  The next two attributes willmake more sense when we get to higher dimensions """

#ndim
""" The attribute "ndim” represents the number of array dimensions or the rank of the array, in this case one. """
print(b.ndim)

#shape
""" The attribute "shape” is a tuple of integers indicating the size of the array in each dimension. """
print(b.shape)

#Numpy array with real numbers
""" We can create a numpy array with real numbers.  """
c=np.array([3.1,11.02,6.2,213.2,5.2])

print(type(c)) # numpy.ndarray
""" If we examine the attribute "dtype," we see float 64 as the elements are not integers.  """
print(c.dtype) # float64

#Indexing and Slicing
""" We can change the first element of the array to 100, as follows. """

d=np.array([20,1,2,3,4])

d[0]=100

print(d) # [100   1   2   3   4]

""" Like lists and tuples, we can slice a numpy array. The elements of the array correspond to the following index. """

e=np.array([20,1,2,3,4])

""" Like lists, we do not count the element corresponding to the last index. """

f=e[1:4]
print(f) # [1 2 3]

""" We can assign the corresponding indexes to new values as follows."""

e[3:5]=300,400
print(e) #[ 20   1   2 300 400]

#BASIC OPERATIONS
""" Numpy makes it easier to do many operations that are commonly performed in data science.
These same operations are usually computationally faster and require less memory in numpy compared to regular Python. """

#Vector addition and subtraction
""" Vector addition is a widely used operation in data science. """

""" The new vector 'z' is constructed by connecting the base of the first vector 'u' with the tail of 
the second 'v'. The following 3 lines of code will add the two lists and place the result in the list 'z'. """
u0=[1,0]
v0=[0,1]
z0=[]

for n, m in zip(u0,v0):
    z0.append(n+m)

print(z0) # [1, 1]

""" We can also perform vector addition with one line of numpy code. """
u2=np.array([1,0])
v2=np.array([0,1])
z2=u2+v2 # [1, 1]

""" It would require multiple lines to perform vector subtraction on two lists """


u3=[1,0]
v3=[0,1]
z3=[]

for n, m in zip(u3,v3):
    z3.append(n-m)

print(z3) # [1, -1]

""" We can also perform vector subtraction by changing the addition sign to a subtraction sign. """
u4=np.array([1,0])
v4=np.array([0,1])
z4=u4-v4 # [1, -1]

#Array multiplication with a Scalar
""" Vector multiplication with a scalar only requires one line of code using Numpy. """

h=np.array([1,2])
i=2*h  #[2, 4]

""" It would require multiple lines to perform the same task as shown with python lists, in addition, the operation
would also be much slower. """
h2=[1,2]
i2=[]

for n in h2:
    i2.append(2*n)

print(i2)  #[2, 4]

#Product of two numpy arrays
""" Hadamard product is another widely used operation in data science. We can also perform Hadamard product with 1 line of code in Numpy. """
e=np.array([1,2])
f=np.array([3,2])
g=e*f   #[3, 4]

""" It would require multiple lines to perform Hadamard product on two lists """

e2=[1,2]
f2=[3,2]
g2=[]

for n, m in zip(e2,f2):
    g2.append(n*m)

print(g2) #[3, 4]

#Dot product
""" The dot product is another widely used operation in data science. The dot product is a single number given and represents how similar two vectors are. """

""" We multiply the first component from 'j' and 'k'. We then multiply the second component and add the result together.
The result is a number that represents how similar the two vectors are. """

j=np.array([1,2])
k=np.array([3,1])

# 1*3 + 2*1 = 5

result = np.dot(j,k) # 5

#Adding constant to an numpy Array
""" Consider the array 'l'. The array contains the following elements."""

l=np.array([1,2,3,-1])

""" If we add a scalar value to the array,  numpy will add that value to each element. This property is known as broadcasting.  """
ls= l+1  # 1+1, 2+1 ,3+1 , -1+1] = [2,3,4,0]

#UNIVERSAL FUNCTIONS
""" A universal function is a function that operates on ndarrays. 
We can apply a universal function to a Numpy array."""

#Mean
""" We can calculate the mean or average value of all the elements in 'a' using the method "mean”. 
This corresponds to the average of all the elements. In this case the result is zero. """

m=np.array([1,-1,1,-1]) 
mean_m=m.mean() # 1/4 (1-1+1-1)

#Max
""" We can find the maximum value using the method max """

n=np.array([1,-2,3,4,5])
max_n=n.max() # 5

#Min
""" We can find the smallest value using the method min """

n2=np.array([1,-2,3,4,5])
min_n=n2.min() # -2

#std
""" Get the standard deviation of numpy array """
standard_deviation=n.std() #2.4819347291981715

#Sin
""" We can use numpy to create functions that map numpy arrays to new numpy arrays. """

o=np.array([0, np.pi/2,np.pi]) #We can accessthe value of pi in Numpy in this way.

""" We can apply the function "sin" to the array 'o' and assign the values to the array p; this applies the sine function to each element in the array. """
p=np.sin(o) 

""" This corresponds to applying the sine function to each component of the vector. 
The result is a new array y where each value corresponds to a sine function being applied to each element in the array 'o' """
print(p) #[0, 1, 1.2e-16]

#Linespace
""" A useful function for plotting mathematical functions is "linespace". Linespace returns evenly spaced numbers 
over a specified interval. 
1)We specify the starting point of the sequence. 
2)The ending point of the sequence. 
3)The parameter "num" indicates the Number of samples to generate, in this case, 5.
The space between samples is 1.
"""

q=np.linspace(-2,2,num=5) #[-2, -1,  0,  1,  2]

""" f we change the parameter num to 9, we get 9 evenly spaced numbers over the interval from -2 to 2. """
r=np.linspace(-2,2,num=9) #[-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]

#PLOTING MATHEMATICAL FUNCTIONS
""" We can use the function linespace to generate 100 evenly spaced samples from the interval 0 to 2 pi. """

s=np.linspace(0,2*np.pi,100)

""" We can use the Numpy function sin to map the array s to a new array t. """
t=np.sin(s)

import matplotlib.pyplot as plt
"""  We can import the library pyplot as plt to help us plot the function. """

plt.plot(s,t)

test1 = np.array([1,-1])*np.array([1,1])
print(test1)

test2 = np.dot(np.array([1,-1]),np.array([1,1]))
print(test2)
