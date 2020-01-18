def div(a,b):
    print(a/b)

div(6,2)
div(2,4)
"""
    In here the position is vitaly important    
"""
"""
    What if we want to make sure the numerator is always greator than denominator     
    def div(a,b):
        if a<b:
            a,b=b,a
        print(a/b)
        
        although think of a situation in which this div() function is not available for editing for you
        as it is other file,or you are not permited to make changes in the div() 
        so in that case , you can use decorator
        by Decorator you can make some changes to the other function
"""
print()

# Here we will make a new function (decorator) which will make changes to other function
def smart_div(func):                # So we have a function as perameter in a function
    def inner(a,b):
        if a<b:
            a,b=b,a                 # Swaping
        return func(a,b)
    return inner

div= smart_div(div)

div(2,4)

"""
    So with python we can change the code of some existing function without even touching 
    that function itself
    We can't do so in other languages
"""
