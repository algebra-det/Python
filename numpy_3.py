from numpy import *

#Aliasing
print("ALIASING")
arr = array([2,6,5,8,4,5,9])

arr1 = arr          # Aliasing , means pointing to a certain address

print("arr ",arr)
print("arr ",arr1)

print("id of arr ",id(arr))
print("id of arr1",id(arr1))

arr1[1] = 7             # As for arr and arr1, we are aliasing so the index value of both
print("arr ",arr)       # the elements at index 1 will change of both arr and arr1
print("arr1 ",arr1)
print()

""" 
    When we use arr = arr1 , we don't actually have 2 arrays now as arr and arr1
    we have a single array , both arr and arr1 are pointing at the same array 
    This is also called "Aliasing" 
"""

# Actual Coping - 1.Shallow Copying , 2. Deep Copying

# 1.Shallow Copying - Linked
print("VIEW() - SHALLOW COPYING ")

arr2 = arr.view()       # .view() actually copies the array and hence have a different address
print("arr2 ",arr2)             # So here we are not Aliasing , we are actaully creating another array
print("id of arr2",id(arr2))         # with same elements that of arr

arr2[1]= 91             # As we used .view() , it has done shallow copy
print("arr ",arr)       # Hence Both the elements of arr and arr2 will change
print("arr2 ",arr2)     # same as above in aliasing

""" In view() the two arrays are linked to each other"""

# 2.Deep Copying - Not linked
print("COPY() - DEEP COPY")

arr3 = arr.copy()               # .copy() copies the array with different address just like view
print("arr3 ",arr3)             # difference is that in this , if we change value of arr3
print("id of arr3 ",id(arr3))   # the value of arr i.e. the array from which we have copied will remain untouched

arr3[1]= 56                     # As we used .copy() , it has done deep copy
print("arr ",arr)               # Henced The array from which we copied will ramain intact
print("arr3 ",arr3)             # change will only take place at the copied array

"""  In copy() , the two arrays are not linked to each other"""


























