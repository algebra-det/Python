""" ways of implementing POLYMORPHISM
    1. Duck Typing
    2. Operator Overloading
    3. Method Overloading
    4. Method Overriding
"""
# Duck Typing

class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):     # ide will work with Pycharm.execute as well as MyEditor.execute
        ide.execute()


idle = Pycharm()
editor = MyEditor()

lap1 = Laptop()
lap1.code(idle)
print()
lap1.code(editor)

"""
    if ide is of class MyEditor in our case 'idle' it will go to MyEditor.execute
    if ide is of class Pycharm in our case 'editor' it will go to Pycharm.execute
    The only requirement is that the classes must have an execute method 
    
    For Duck Typing , there is a saying that
    if there is a bird, that walks like a duck , quacks like a duck and swims like a duck,
    than it is a duck.
    So In our case "ide" of class "laptop" is an epitome of Duck in duck typing
"""










