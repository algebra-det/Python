from numpy import *

arr = array([
                [1,2,3,4],
                [5,6,7,8]
            ])

m = matrix(arr)         # We have a function to define that it's a matrix
print("M:-\n",m)
""" The output of this will look like simple multiple dimensional array
    but we can do the matrix work with this"""

n = matrix('1,2,7,8 ; 3,5,2,6 ; 6,2,4,8 ; 9,7,5,3')     # If we are using string, or taking input from the user
print("N:- \n",n)                                                # 4X4 Matrix

# if we want to print diagonal elements fo the matrix
print("Diagonal elements of N - ",diagonal(n))

print("Maximum value element in N ",n.max())

# Multiplication of Matix
""" You remember how we have to multiply two matrices
    we have to multiply every row with every column
    Python have it inbuilt, if we simply put * to multiply , python will know its for matrix
    and will do the heavy multiplication for us"""

m1 = matrix('1,2,3,4 ; 5,6,7,8 ; 4,5,6,7')      # 3X4
m2 = matrix('7,6,5,4 ; 8,7,6,5 ; 4,3,2,1')      # 3X4

m3 = m1 * m2;
print(m3)

""" If we haven't used the matrix() , then python will not know that we want to use
    the matrix's multiplication format, and hence it should have done the simple multiplication"""









