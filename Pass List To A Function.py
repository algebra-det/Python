from array import *

# Function
def count(lst):
    erray= array('i',[])
    orray= array('i',[])
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
            erray.append(i)
        else:
            odd+=1
            orray.append(i)
    return even,odd,erray,orray


# Main
lst = array('i',[])
x = int(input("How many values do you  want to add to the list"))

for i in range(x):
    a = int(input("Enter the element"))
    lst.append(a)

print(lst)
print(lst.buffer_info())
print(len(lst))
even , odd , erray , orray = count(lst)
print("Even terms are : ",even)
print(erray)
print("Odd terms are : ",odd)
print(orray)
print()

print("Even : {} and Odd : {}".format(even,odd,theyare=6))


""" This Format function 
    in this we have to pass strings
    it will insert the given string values in curly brackets{}
"""