from numpy import *
""" At arr4 , we see the addition of two array elements, is also called VECTORIZED OPERATION"""

arr = array([1,2,3,4,5])
arr2 = array([],int)
for i in arr:               # For adding 5 to every element in arr and hence creating new arr2
    j = i+5
    arr2 = append(arr2,j)   # For appending we have to use this syntax
print(arr2)

#OR

arr3 = arr +5               # Simple way of operating anything in array
print(arr3)

arr4 = arr2 + arr3          # Can also add elements of two or more arrays
print(arr4)                 # Also called as Vectorized Operation

print("Sin ",sin(arr4))            # For sin values of each element
print("Cos ",cos(arr4))            # For cos values of each element
print("Log ",log(arr4))            # For log values of each element
print("Square root ",sqrt(arr4))   # For square roots of each element

print("Sum of all ",sum(arr4))     # Will give the total sum of array elements
print("Minimum value ",min(arr4))  # Minimum value from the array
print("Maximum value ",max(arr4))  # Maximum value from the array
print("Sorted ",sorted(arr4))      # Sorted array