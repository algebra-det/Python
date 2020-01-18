

"""
def great():
    print("Hello")
    great()                     #calling function itself is called recursion

great()

    As if a function call itself it will go infinite times
    but here in python there's a limit to recursion set by itself
    which is 1000 times
    you can check out the limit by importing module 'sys'
    print(sys.getrecursionlimit())    
    
"""

import sys

print(sys.getrecursionlimit())      #it will show 1000

""" 
    However if you want to increase the limit
    you can do so by
    sys.setrecursionlimit('any number')
    for example,
                sys.setrecursionlimit(2000)
"""
sys.setrecursionlimit(2000)

i = 0                   # variable taken to count the number of times hello is printed

def great():
    global i
    i+=1
    print("Hello",i)
    great()

great()
