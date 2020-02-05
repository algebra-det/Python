"""
    Their are three types of methods
    1. Instance Methods (it has SELF in it)--> 1. Accessor Methods , 2. Mutator Methods
    2. Class Methods (it has CLS in it)
    3. Static Methods
"""
class student:

    school = "Nagar"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):                               #Accessors method or getter
        return self.m1                              #           |
                                                    #   both are INSTANCE METHODS AS THEIR IS (self)
                                                    #           |
    def set_m1(self,value):                         #Mutator method or setter
        self.m1 = value

    @classmethod                                    # for class method we have to declare @classmethod , it is a decorator
    def schools(cls):                               # Class Method as it has (cls) in it
        return cls.school

    @staticmethod                                   # for static method we have to declare @staticmethod
    def info():                                     #static method as it has (nothing) in it
        return "This is Student school"

s1 = student(23,6,85)
s2 = student(95,82,4)

print("Average of s1 ",s1.avg(),s1.school)
print("Average of s2",s2.avg(),s2.school)

print(s1.get_m1())                                  #calling accessor method
s2.set_m1(56)                                       #calling mutator method

print("Average of s1 ",s1.avg())
print("Average of s2",s2.avg())

print(student.schools())                               #calling class method

student.school = "Colony"
print(student.schools())

print(student.info())                                      #calling static method
