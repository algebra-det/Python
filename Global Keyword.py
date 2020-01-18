
a = 10                              # This one is global variable

def something():
    a = 15                          # This one is local variable
    b = 16                          # This one is local variable too
    print("Inside ",a)

something()
print("Outside ",a)
 # print(b) it will not take affect outside the function as b is a local vaiable

def something1():
    print("In Something1 a is ",a)      # As there is no declaration of
                                        # a in this function
                                        # So it will take value from
                                        # global variables
something1()

""" 
    If we want to change the value of global variable permanently from within a function
    than we can do so by declaring 'global (variable name)' inside funciton     
    
"""


def something2():
    global a                            # Declaration for changing the value of global variable permanently
    a = 14
    print("Inside something2: ",a)

something2()
print("Outside : ",a)

