class A:

    def show(self):
        print("In A show")

class B:
    pass


a1 = A()
a1.show()

b1 = B()
#b1.show()       # this will not work as show is not present in class B

print("__________")

class Al:

    def show(self):
        print("In A show")

class Bl(Al):
    pass


al1 = Al()
al1.show()

bl1 = Bl()
bl1.show()       # as Bl has inherited Al, so if it does not have show() than it will go to parent class
                 # for executing show() method

print("________")

class Alp:

    def show(self):
        print("In A show")

class Blp(Alp):

    def show(self):
        print("In B show")

alp1 = Alp()
alp1.show()

blp1 = Blp()
blp1.show()       # Now as we have show() in Class Blp, SO it will not go to parent class for show()
                  # Hence it will execute the show() method of it's own class