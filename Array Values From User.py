"""
    Here we will learn how to take array values from the user

"""

from array import *

arr = array('i',[])

y = int(input("Enter the length of the array "))

for z in range(y):
    a = int(input("Enter the next value "))
    arr.append(a)

print(arr)

b = int(input("which number do you want to search "))
# Searching manually i.e. without inbuilt function

d=0
for c in arr:
    if c==b:
        print("its at index ",d)
        break
    d+=1
else:
    print("It does not match any value you entered")

print()
print()
print()
# searching with function

print("It's at : ",arr.index(b))