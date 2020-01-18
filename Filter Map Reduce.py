
num = [1,6,9,5,3,45,8,7,2,1,5,9,5,3,4,8,6]

def is_even(n):
    return n%2==0

#OR

a = lambda n:n%2==0

even = list(filter(is_even,num))
even2 = list(filter(a,num))                 #filter function

print("even is ", even)
print("even2 is ",even2)

""" Defining lambda function for single use"""
even3 = list(filter(lambda n:n%2==0,num))       #defining lambda inside a function as it's for single use
print()
print("even3 is ",even3)

"""
     This filter function is used to filter , with this function we have to pass filter(__function,__itereable)
     So passing function name and the iterable value
     funcion = function_name 
     iterable = List_name
     In above we explained the function with name lambda in filter function itself
     as it was for single use

"""

# if we want to take the return value and then make some operations on them
# We use map()
print()
even4withdouble = list(map(lambda n : n*2,even3))   #taking input from above even3
print("even4withdouble is ",even4withdouble)
print("even4sum is",sum(even4withdouble))

# Reduce() is used to have single return value from iterables
# for example if we want to add all the return value from even
# It is not available by default, from functools import reduce
print()

from functools import reduce

def add_all(a,b):
    return a+b

sum = reduce(add_all,even4withdouble)
print("Sum is ",sum)
#OR
sum1= reduce(lambda a,b:a+b , even4withdouble)
print("\nSum1 is ",sum1)