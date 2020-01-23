
from numpy import *
"""  Array() , Linspace(), Logspace(), Arange(), Zeros(), Ones() """
"""  %f means with decimal"""
"""  %d means without decimal"""
"""  By default array creates array with float value to have array with integer value
     We have to define int after the putting array values  like in arr below"""

arr = array([1,2,3,4,5,6],int)
print(arr)
print("%.3d"%arr[1])        # Here %.3d means it will give integer value with 3 zeroes before value
print("%.3f"%arr[1])        # Here %.3f means it will give float value with 3 digits after decimal value

arr1 = linspace(1,40,20)        #this will give - start with 1 and end with 40 but have 20 steps
print(arr1)

arr2 = arange(1,40,2)          # Works as Range, start with 1 , end with 40 , iterate 2 jumps
print(arr2)

arr3 = logspace(1,40,5)        # logspace make 10**x means it will give - 10 raise to the power
print(arr3)                     # Hence it will start with 10**1 and end with 10**40 with 5 steps/parts
print("%.2f"%arr3[4])           # Here .2 means print value with 2 digits after decimal
print("%.6f"%arr3[4])           # Here .6 means 6 digits aftere decimal
print("%.6d"%arr3[4])

arr4 = zeros(5)                 # Will create 5 elements of value 0
print(arr4)

arr5 = ones(6)                  # Will create 6 elements of value 1
print(arr5)

arr6 = ones(4,int)
print(arr6)











