from array import *

# Functions

def arraying(h):
    for z in range(h):
        a = int(input("Enter the value "))
        x.append(a)
    for m in x:
        print(m, end=",")
    print()


def appending():
    d = int(input("By how many more values"))
    for e in range(d):
            f = int(input("Enter the value "))
            x.append(f)
    for l in x:
        print(l, end=",")
    print()
    more()


def more():
    c = int(input("\nDo you want to append the array?\nIf YES than press '1' :- "))
    if c ==1:
        k = appending()
    else:
        print("OK\nBBYE")

# Main

x = array('i',[])
print(id(x))
y = int(input("How many elements do you want to add in array:- "))

arraying(y)                 # this funciton can also be defined to return value\
                            # but as we have declared to print values in function
                            # so there's no need to return value
more()
print(id(x))
print("The Final Array is :- ")
for z in x:
    print(z,end=",")


