# Multiplication of Matrix
"""
Few specifications of numpy.dot:

    If both a and b are 1-D (one dimensional) arrays -- Inner product of two vectors (without complex conjugation)
    If both a and b are 2-D (two dimensional) arrays -- Matrix multiplication
    If either a or b is 0-D (also known as a scalar) -- Multiply by using numpy.multiply(a, b) or a * b.
    If a is an N-D array and b is a 1-D array -- Sum product over the last axis of a and b.
    If a is an N-D array and b is an M-D array provided that M>=2 -- Sum product over the last axis of a and the second-to-last axis of b:

Also, dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
"""

from numpy import *

alpha = array([[1,2,9],[3,4,5],[98,56,21]])
beta = array([[7,9,1],[2,6,3],[41,32,12]])
print(alpha.dtype)
print(alpha.ndim)
print('Alpha array is :')
for i in alpha:
    print(i)
print("Beta array is :")
for i in beta:
    print(i)

gamma = multiply(alpha,beta)    # OR gamma = alpha * beta
print("Multiplication of alpha and beta : -\n",gamma)

zeta = alpha.dot(beta)      # OR zeta = alpha @ beta
print("Dot-Product of alpha and beta :-\n",zeta)


"""
    If we have used matrix instead of array than *,.dot & @ would have given the matrix multiplication
    as we used array thats why matrix type multiplication is possible via .dot & @
"""

hello = matrix([[2,3],[5,6]])
bello = matrix([[9,8],[6,3]])
print(hello@bello)
print(hello.dot(bello))
print(hello*bello)
print(multiply(hello,bello))

delta = array([[1,2,9],[3,4,5],[98,56,21]])
theta = array([[7,9,1],[2,6,3],[41,32,12]])
print(delta@theta)
print(delta.dot(theta))
print(delta*theta)
print(multiply(delta,theta))
