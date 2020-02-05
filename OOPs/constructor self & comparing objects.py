""" Constructor is the one that allocates memory to objects based on their number of variables"""

class computer:
    def __init__(self,h):               # init is also called constructor
        self.name = "akash"
        self.age = 22
        self.h = h

    def config(self):
        print(self.name,self.age,self.h)

    def update(self):                   # Self is used to point to the object
        self.age = 21

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False



c1 = computer("hero")
c2 = computer("not hero")

c1.config()
c2.config()
# Comparing Objects
if c1.compare(c2):                      #Compare is not a built-in function we have to define it in class
    print("They are same")              # here we have self,other --> c1(self).compare(c2(other))
else:
    print("They aren't same")
print()

c1.name = "Mickey"
c2.age = 23
print(c1.name,c1.age)
print(c2.name,c2.age)
print(c1.h)
print(c2.h)
if c1.compare(c2) == False:
    print("They aren't same")
else:
    print("They are same")
print()


c1.update()
c1.config()
c2.config()

c2.update()
print(c1.name,c1.age)
print(c2.name,c2.age)
if c1.compare(c2):                      #Compare is not a built-in function we have to define it in class
    print("They are same")              # here we have self,other --> c1(self).compare(c2(other))
else:
    print("They aren't same")