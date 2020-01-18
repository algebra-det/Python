print(__name__)

# Check out the hello.py file , as that is also a module
# If we import with 'import hello' it will also import the print statement in that hello file

import hello                        #This will print the print staement along with its module name instead of __name__
print("SO here is ",__name__)
print(" here is "+__name__)

print()
import hello2                       #Importing executes all the statements from the importing module
print("It's ME")
hello2.add()

"""
    as importing executes all the statement from the importing module, we make the modules with only defining functions
    and no calling statements in the importing module
    So this __name__ comes handy when we want not to execute the calling functions from the importing module
"""