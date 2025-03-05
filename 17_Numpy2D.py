#2-Dimensional Numpy Arrays
""" We can create Numpy arrays with more than one dimension.
This section will focus only on 2D arrays, but you can use Numpy to build arrays of much higher dimensions. 

We will cover the basics and array creation in 2D, 
indexing and slicing in 2D, 
and basic operations in 2D."""

import numpy as np

""" The list contains three nested lists each of equal size. """
a1 = [[11,12,13],[21,22,23],[31,32,33]]

""" We can cast the list to a numpy array as follows. """
A1=np.array(a1)

""" It is helpful to visualize the Numpy array as a rectangular array; each nested list corresponds
to a different row of the matrix. 

The convention is to label this axis 0 and this axis 1 as follows.

         <----Axis 1----->   |
            |11 12 13|       |
         A1:|21 22 23|    Axis 0
            |31 32 33|       |
                             |
"""
""" It's useful to think of "ndim" as the number of nested lists. """

print(A1.ndim )  # 2

""" As with the 1d array, the attribute "shape" returns a tuple."""
print(A1.shape) #(3, 3)


""" The first element in the tuple corresponds  to the number of  nested lists contained in the original list, in this case 3.
The second element corresponds to the size of each of the nested lists.
 
                     A1 = [[11,12,13],[21,22,23],[31,32,33]]             """


""" We can also use the attribute size to get the size of the array. We see there are three rows and three columns. 
Multiplying the number of columns and rows together we get the total number of elements, in this case 9."""

print(A1.size) #9

""" We can use rectangular brackets to access the different elements of the array.

A1[A1[0][0],A1[0][1],A1[0][2],A1[1][0],A1[1][1],A1[1][2],A1[2][0],A1[2][1],A1[2][2]]

            |A1[0][0] A1[0][1] A1[0][2]|
         A1:|A1[1][0] A1[1][1] A1[1][2]|
            |A1[2][0] A1[2][1] A1[2][2]|
"""


""" We can also use a single bracket to access the elements as follows. Consider the following syntax.
This index corresponds to the second row. And this index, the third column. The value is 23. """

print(A1[1][2]) #23

""" We can also use slicing in numpy arrays. The first index corresponds to the first row. The second index accesses the first two columns. """

print(A1[0,0:2]) #[11 12]

""" Consider this example. The first index corresponds to the last two rows. The second index accesses the last column. """

print(A1[0:2,2]) #[13 23]


#ADD ARRAYS
""" We can also add arrays; the process is identical to matrix addition.

Consider the matrix X.

     |1 0|
   X=|0 1|

Consider the matrix Y.

     |2 1|
   Y=|1 2|

We can add the matrices.
   
This corresponds to adding the elements in the same position. 

           |1+2 0+1|
       X+Y=|0+1 1+2|
       
       
The result is a new matrix that is the same size as matrix Y or X.
Each element in this new matrix is the sum of the corresponding elements in X and Y.

           |3 1|
       X+Y=|1 3|     """


""" To add two arrays in numpy we define the array in this case X."""
X1=np.array([[1,0],[0,1]])

""" Then we define the second array Y. """
Y1=np.array([[2,1],[1,2]])

""" We add the arrays. """
Z1=X1+Y1

""" The result is identical to matrix addition.  """
print(Z1) #[[3 1] [1 3]]

#MULTIPLY ARRAYS BY THE SCALAR  
""" Multiplying a Numpy array by a scalar is identical to multiplying a matrix by a scalar. Consider the matrix Y, if we 
multiply the matrix by the scalar 2 we simply multiply every element in the matrix by 2. The result is a new matrix of 
the same size where each element is multiplied by two.
"""
Y2 = 2*Y1  #[[4 2] [2 4]]

#MULTIPLICATION OF TWO ARRAYS
""" Multiplication of two arrays corresponds to an element-wise product or Hadamard product. Consider array X and array Y.
Hadamard product corresponds to multiplying each of the elements in the same position.

     |1 0|        |2 1|           |(1)2 (0)1|
   X=|0 1|      Y=|1 2|       X°Y=|(0)1 (1)2|

The result is a new matrix that is the same size as matrix Y or X.
Each element in this new matrix is the product of the corresponding elements in X and Y.

           |2 0|
       X°Y=|0 2|          """

X3=np.array([[1,0],[0,1]])

Y3=np.array([[2,1],[1,2]])

Z3=X3*Y3  #[[2 0] [0 2]]

#MATRIX MULTIPLICATION
""" We can also perform matrix multiplication with numpy arrays.
Matrix multiplication is a little more complex, but let's provide a basic overview. 

Consider the matrix "A",

  |0 1 1|
A=|1 0 1|

Also, consider the matrix "B"

  |1  1|
B=|1  1|
  |-1 1|
  
In linear algebra, before we can multiply matrix "A" by matrix "B" we must make sure that the number of 
columns in matrix "A", in this case 3, is equal to the number of rows in matrix "B", in this case 3.

For matrix multiplication to obtain the i-th row and j-th column of the new matrix we take the dot product of 
the i-throw of "A" with the j-th columns of "B".

--------->    |
  |0 1 1|     |   |1  1|
A=|1 0 1|     | B=|1  1|
              V   |-1 1|

For the 1st column 1st row, we take the dot product of the 1st row of "A" with the first
column of "B" as follows, The result is 0.

0x1 +1x1 +(-1)x1 = 0  

For the first row and the second column of the new matrix we take the dot product of
the first row of the matrix "A" but this time we use the second column of matrix "B"; the
result is 2.

0x1 +1x1 +(1)x1 = 2  

For the second row and the first column of the new matrix we take the dot product of
the second row of the matrix "A" with the first column of matrix "B"; the result is 0.

1x1 +0x1 +(-1)x1 = 0

Finally, for the second row and the second column of the new matrix we take the dot product
of the second row of the matrix "A" with the second column of matrix "B"; the result is 2.

1x1 +0x1 +(1)x1 = 2

    |0 2|
A B=|0 2|

"""


""" In numpy we can define the Numpy arrays "A" and "B". We can perform matrix multiplication and assign it to array "C". """

A2= np.array([[0,1,1],[1,0,1]])
B2= np.array([[1,1],[1,1],[-1,1]])
C2=np.dot(A2,B2)  #[[0 2] [0 2]]

Atest = np.array([[1,2],[3,4],[5,6],[7,8]])
print(Atest)

A = np.array([[1,2],[3,4],[5,6],[7,8]])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
np.dot(A,B)