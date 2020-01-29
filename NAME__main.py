def add():
    print("Welcome User")

def sub():
    print("Not welcome user")

def ifmain():
    add()
    sub()


if __name__=="__main__":
    ifmain()


"""
    This if statement where we used __name__
    we are making sure that if we are executing the hello2.py file as standalone file means not using it as module in other file
    than only it will execute the ifmain() function
    AND 
    if we are using it as module in other file than it will not call ifmain() functionon its own
    
"""
