from numpy import *

a = array([[1,2,3,4],[6,5,9,7]])
c = a

newarray = append(a,[10,12,56,89])     # append
newarray = newarray.reshape(1,3,4)
print(newarray)


a = append(a,[10,9,5,8,6,3,2,1,4,5])
print("A is ",a)
a = a.reshape(1,3,6)
print("a \n",a)
print("a is dimensional ",a.ndim)       # to give the dimension of array

b = array([[200],[96]])
print("b \n",b)
print("b is dimensional ",b.ndim)

mewarray = append(c,b,axis=1)       # axis 1 is used for column adding
print("mewarray \n",mewarray)
print(mewarray.ndim)
print(mewarray.size)                # gives the no. of elements of an array

d = array([[56,765,256,908]])
ora = append(c,d,axis=0)                # axis 0 is used for row adding
print("ora is \n",ora)


mewarray = insert(mewarray,0,45)        # insert is used to insert an element in array at specific index
print(mewarray)

mewarray = delete(mewarray,0)           # delete is used to delete an element at specifix index
print(mewarray)

print("200 is found at index : ",where(mewarray == 200))    # gives the index value of any element but it also gives the datatype too
h = where(mewarray == 200)                                  # to print only the index we will store the result of where in a variable
print("200 is found at index : ",h[0])                      # and print the index of this variable at 0
