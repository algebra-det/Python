a = 3
b = 9

print(a+b)
print(int.__add__(a,b))     # when we use + , the int.__add__(a,b) is called automatically
print(a.__add__(b))         # "add" method of "int" is called

print(abs(5.3654))

a = '3'
b = '9'

print(a+b)
print(str.__add__(a,b))     # "add" method of "str" is called
print(a.__add__(b))
print()
""" The __add__ method of str<class>, int<class> , float<class> ,etc are predefined/in-built"""

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    """ Now if we make an object of class student i.e. s1,s2 in our case, how can we add such objects.
        As __add__ for our defined 'student<class>' is not built-in , so we have to make
        an __add__ method for our class"""

    #The making of our own class operator working is called Operator_Overloading
    def __add__(self, other):       # we make our own __add__ method for our defined "Student" class
        m1 = self.m1 + other.m1     # if we use + operator , it will automatically call __add__
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

s1 = student(23,45)
s2 = student(87,99)

s3 = s1+s2
print(s3.m1)
print(s3.m2)

""" Hence many methods can be created for multiple puroposes which will work on our defined class
    for example, we can create __sub__ , __mul__ , __div__ which corrensponds to -,*,/"""

# Lets make another class in which we will create more methods you can check the availablity
# of methods by pressing <ctrl>+<space_bar>

class student1:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):       # Same as before
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    def __gt__(self, other):        # if we use > or < , than it will automatically call __gt__ method
        x = self.m1 + self.m2
        y = other.m1 + other.m2
        if x>y:
            return True
        return False

stu1 = student1(66,45)
stu2 = student1(27,79)

stu3 = stu1+stu2
print(stu3.m1)
print(stu3.m2)

if stu1 > stu2:
    print("Student1 is greater")
else:
    print("Student2 is greater")

j = 9
print(j)    # when we just call "j" , it automatically calls __str__ method
print(j.__str__())

print(stu1)         # we don't have __str__ method for our 'student<class>' so it will return the address of the object
print(stu1.__str__())

""" Lets make this thing work , we will make __str__ for our class which will return
    our stated result"""

class student2:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):       # Same as before
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    def __gt__(self, other):
        x = self.m1 + self.m2
        y = other.m1 + other.m2
        if x>y:
            return True
        return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

st1 = student2(12,84)
st2 = student2(54,23)

k = 9
print(9)
print(k.__str__())

print(st1)              # Now it will return the value of our object
print(st1.__str__())

print(st2)

"""
    Creating any operator like addition(+), subtraction(-), multiplication(*),division(/),
    when we will perform any operator , behind the scene we are calling methods of such operators
    respectively.
    when we press + , it goes to __add__
    when we press - , it goes to __sub__
    when we press * , it goes to __mul__
    when we press / , it goes to __div__
    when we press > or < , it goes to __gt__
    ...
"""

