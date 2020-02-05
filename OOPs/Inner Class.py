class student:                                  #OUTER CLASS

    def __init__(self,name,rollno,marks):
        self.name = name
        self.roll = rollno
        self.marks = marks
        self.lap = self.laptop()

    def show(self):                             # 1st show method for outer class
        print(self.name,self.roll,self.marks,self.lap.brand,self.lap.cpu,self.lap.ram)
        #OR
        self.lap.show()

    # Suppose the student also have laptops and we want to take input of the laptop names
    # We can do so without changing the anything in __init__
    # i.e. by making another class inside a class

    class laptop:                       #INNER CLASS

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "16"

        def show(self):                         #2nd show method for inner class
            print(self.brand,self.cpu,self.ram)

s1 = student('akash',2,98)
s2 = student('Mickey',3,85)

s1.show()
s2.show()
print()
print(s1.lap.brand)
#OR
lap1 = s1.lap                       #We are creating an object for s1.lap class
lap2 = s2.lap                       #We are creating an object for s2.lap class
                                    #Hence it will be easy to write them

print(lap1.brand)

s1.lap.cpu = "i3"
lap2.cpu = "i7"
s1.show()
s2.show()

print()

lap1.show()
lap2.show()

