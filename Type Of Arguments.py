
"""
    Formal Arguments:
    Actual Arguments:- Position
                       Keyword
                       Default
                       Variable Length


"""

def add(a,b):                       #when defining , a,b are called formal arguments
    c = a+b
    print(c)

add(3,5)                            #when calling, these are called actual arguments

print()

def person(name,age):
    print(name)
    print(age-5)
person('akash',22)                  # Position Actual Argument
                                    # Here position plays a great role
                                    # As 'akash' is at same position as 'name'
print()

""" In case if we don't know the position than"""
person(age=22,name='akash')         # Keyword Actual Argument
                                    # Here we use keywords to arguments

""" For default , we define any parameter as default
    As if the user don't input the value ,in our case 'age', than 
    Age will be declared the default value defined by the programmer
"""
def persons(name,age=18):           # Here we are declaring DEFAULT for age
    print(name)
    print(age)

persons('akash')
persons('akash',22)

""" Variable length actual argument
    Through this we can define the function where the number of arguments are not fixed
     for example,
            if the user gives more than two arguments for sum      
"""
print()

def sum(x,*y):                      # we define variable length with *y
                                    # Here y will  become a tuple to contain many values
    """Here is a catch , we can't modify the value of tuple by just
        doing c= x+y
    """
    #so

    for i in y:
        x = x + i
    print(x)

sum(9,5,6,9)

# The above sum function can also be defined by
print()

def sum1(*b):
    x=0
    for i in b:
        x = x+i
    print(x)

sum(9,5,6,9)

