from array import *

class human:
    def walk(self):
        print("Walking")

me = human()                 # here me is object of our definned classs walk
myself = human()
a = 'mine'                  # here a is an object of class str
b = 5                       # b is an object of class int
c = array('i',[2,6])        # c is an object of class array

print("me is ",type(me))
print("a is ",type(a))
print("b is ",type(b))
print("c is ",type(c))

""" This Syntax is more used than the other one """
me.walk()                       # object.method which is of our defined class and method
myself.walk()
print(a.capitalize())              #object.method which is of predefined class str
print(a)
print(b.bit_length())              # object.method which is of predefined class int
print(c.buffer_info())             # objeect.method which is of predefined class array

#OR Another way of calling method for object of any class
""" Ohter one"""

human.walk(me)                   # class.method(object) which is of our defined class method
human.walk(myself)
print(str.capitalize(a))           # class.method(object) which is of predefined class str
print(int.bit_length(b))           # class.method(object) which is of predefined class int
print(c.buffer_info())             # class.method(object) which is of predefined class array