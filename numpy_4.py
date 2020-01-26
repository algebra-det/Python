from numpy import *

arr = array([
                [1,2,3,7,8,9],
                [4,5,6,8,6,2],
            ])

print(arr)
print(arr.ndim)

arr1 = array([[1,2,3,4],[5,6,7,8]])
print(arr1)

print("Type of array - ",arr1.dtype)       # Type of Array
print("Dimension of array - ",arr1.ndim)        # Dimension of Array
print("No. of Rows and Columns - ",arr1.shape)      # Gives No. of Rows and Columns
print("Size of the entire block - ",arr1.size)      # Total elements of the array

arr2 = arr.flatten()       # Flattening multidimensional array into one dimensional
print(arr2)

arr3 = arr2.reshape(3,4)        # Breaking one dimensional into multidimensional
print(arr3)                     # So we have 3 Rows and 4 Columns

arr4 = arr2.reshape(2,2,3)      # Meaning to have 2(two) 2-D Arrays having 3 elements each
print(arr4)

arr5 = arr2.reshape(1,6,2)      # As above , have 1(one) 6-D Array having 2 elements each
print(arr5)









