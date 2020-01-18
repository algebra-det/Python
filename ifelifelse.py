"""Here we will learn about if elif & else conditions"""

x = int(input("Enter any number"))

if x==1:
    print("One")
    """
   if we put all "if" than it will check each and every condition
   which will be wasteful for the memory

   if x==2:
        print("Two")

        if x==3:
            print("Three")

    So to overcome this issue we will use "elif" which
    in terms will only be checked if the above condition is not true

    so that it will not go through each and every condition
    once any condition is true ,the elif conditions will not
    be used and compiled

    """

elif x==2:
    print("Two")

elif x==3:
    print("three")

else:
    print("Greater than 4")