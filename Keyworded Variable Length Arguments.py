
def person(name,*data):                 # It's variable length argument
    print(name)
    print(data)
    for i in data:
        print(i)

person('akash', 22 , 'Haryana', 291)
""" As here we don't know what is 22 , haryana or 291
    so while displaying this the user will also don't know
    what they are , however why should he/she entered these in
    the first plave
"""
print()
"""so for these scenerios we use keyword variable length arguments
    in which the user will also define keywords while entering
    unknown and unspecified data"""

def persons(name,**data):
                                        # See there's ** two stars
                                        # It defines that the input will contains two argument type
    print(name)
    for i,j in data.items():
        print(i,j,end=",")

persons('akash',age=22, city='Haryana', add=291)


