from numpy import *

a = array([5,564,231,45,65156,6,1646,56231,9,56])
print("A subset of array a is ",a[2:7])     # Array Slicing

print("A subset of array a is ",a[-3:])     # Negetive Slicing

f = lambda x:x+2                            # anonymous function
print("Array after addition function",f(a))

l = [5,7,3,8,5,7]
print("Type of l ",type(l))
b = array(l)                    # making array from list
print("Type of a ",type(b))

""" We can also make array from tuple"""

# making list from array

d = a.tolist()                  # hence , array to list
print(d)                        # try pressing a.<ctrl>+<space> for more options

savetxt("MyArray.csv",a)        # saving array to .csv file which is microsoft excel

print("Sorted array a - ",sorted(a))    # sorting array , <alternative> is sort


e = array([[20,78,2],[90,87,6]])
print("Element at index e[1][2] is ",e[1][2])
print(e)

# As array E is 2-dimensional
count = 0
for i in e:
    jount = 0
    for j in i:
        print("At count %d and jount %d element is %d"%(count,jount,j))
        jount += 1
    count += 1








