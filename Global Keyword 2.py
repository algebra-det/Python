a = 10
b = 8
c = 3
print("id of global variable a",id(a))
print("Outside a is : ",a)
print()

def something():
    a = 9

    x = globals()['a']                                      # As global will give values of all global variables
    print("id of global a in function ",id(x))              # which in our case is a,b & c
    print("id of local a in function ", id(a))
    print("In something a is : ",a)                         # so we have to define 'a' as we want only the value of a
    print("In something Global a is : ", x)
    globals()['a'] = 15                                      # changing global variable value permanently


something()

print("Outside a is : ",a)

"""
    NOTE: There are two variables with name 'a' in functin
    so by getting global variables value in some other variable
    we can have the values of local as well as global variable
    having the same name by using 'globals()['name of global variable']
            
"""
