""" Here we will talk about Exception Handling, it is used to handle errors
    There are three types of errors:
    1. Compile-Time Error   - suppose if you forgot to insert : after function declaration than it is a syntaxError i.e. compile time error
    2. Logical Error        - as we put 2+3 , we get 4 instead of 5 , which is the wrong output
    3. Run-Time Error       - we are dividing 6 by 0(zero) than it is a divide by zero error, as nothing is divisible by zero
                              it is mostly done by the user, suppose we said to the user to input two values for division
                              and the user input 6 and 0
"""
""" We use Exceptional Handling to make sure our program work continuously even if there's 
    an error produced from the user side , for example , Division by Zero , List index out of range
    Same as we used while making Tic_Tac_Toe game """

a = 5       # Normal Statement = the one which will not return any error
b = 6       # Normal Statement
print(a/b)  # Critical Statement = the one which can return error
print("Bye")

a = 4
b = 0
#print(a/b)  # It will give you an error and also stop the execution right away without printing Bye
print("Bye")

# To counter this we use Try:

j = 7
k = 0
try:
    print(j/k)
except Exception:
    print("Hey , you cannot divide a number by zero")
print("Bye")
print()


l = 9
m = 0
try:
    print(l/m)
except Exception as e:
    print("hey , here you cannot divide a number by zero",e)
print("Bye")
print()

l = 9
m = 3
try:
    print(l/m)
except Exception as e:
    print("hey , here you cannot divide a number by zero",e)
print("Bye")
print()


""" Suppose we are working with database, if we open the database than we must close it too before exeting
    just like we open our fridge and than take our food and than close it """

l = 9
m = 0
try:
    print("Resource Open")
    print(l/m)              # here it will Resource open and then go to except so that there will be no Resource Closed
    print("Resource Closed")
except Exception as e:
    print("hey , here you cannot divide a number by zero",e)
print("Bye")
print()
""" So we should not put the closing in 'try' as if the critical statement execute smoothely than
    there will be closing 
    but if the critical statement return error and goes to except than the database will not be closed
    So we should put the closing in except"""

l = 9
m = 0
try:
    print("Resource Open")
    print(l/m)              # here is a catch too , what if there's no error and so that there will be no closing as there's no
except Exception as e:      # closing in try , so one thing we can do is to have closing in 'try' as well as in 'except'
    print("hey , here you cannot divide a number by zero",e)
    print("Resource Closed")

print("Bye")
print()

l = 9
m = 3
try:
    print("Resource Open")
    print(l/m)
    print("Resource Closed")
except Exception as e:
    print("hey , here you cannot divide a number by zero",e)
    print("Resource Closed")

print("Bye")
print()

""" Another way of doing such is by using 'finally' in try except statement"""

l = 9
m = 0
try:
    print("Resource Open")
    print(l/m)
except Exception as e:
    print("hey , here you cannot divide a number by zero",e)
finally:
    print("Resource Closed")

print("Bye")
print()

""" In above , whether there is an error or not , whether it is divisible or not
    there will be Resource Opening and Resource Closing too after every operation
    
    Finally Blocks will be executed: if we get error as well as if we don't get the error
"""

l = 9
m = 2
try:
    print("Resource Open")
    print(l/m)
    k = int(input("Enter the number = "))
    print(k)
except Exception as e:
    print("hey , here you cannot divide a number by zero",e)
finally:
    print("Resource Closed")

print("Bye")
print()


l = 9
m = 2
try:
    print("Resource Open")
    print(l/m)
    k = int(input("Enter the number = "))
    print(k)
except ZeroDivisionError as e:
    print("hey , here you cannot divide a number by zero",e)

except ValueError as e:
    print("Hey , Invalid Input ,",e)

except Exception as e:
    print("Hey , Something went wrong ",e)

finally:
    print("Resource Closed")

print("Bye")
print()