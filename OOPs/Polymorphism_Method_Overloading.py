""" Method Overloading is 'not available' in python
    lets say if we have Two Methods of same name in a Class<which is not possible in other languages>
    but the thing is these Methods should take different parameters in order to be different in working
    So , having two methods of same name in a class in known as Method Overloading"""


""" As Method Overloading is not available in python
    it is although available in other OOPs langugages Java , C , C# , etc
    Hence we can't make two methods with same name in python
    for example,
        class student:
            def average(a,b):
                <do something>
            
            def average(a,b,c):
                <do something>
"""
"""But there is a way for achieving Method Overloading's Functioning"""

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a,b):      # This take 2 arguments a & b , than it will return addition of these two only
        s = a+b
        return s

s1 = student(50,69)

print(s1.m1,s1.m2)

print(s1.sum(5,6))      # As we are passing two arguments it will work fine
print(s1.sum(5,6,4))    # What if we want to pass three arguments , it will not work and return an error

print()
"""so to have the working of method overloading we can make the sum method to take 1, 2 or even 3 arguments"""

class student1:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None, b=None, c=None):      # So it can take 1 ,2 or 3 arguments and will work accordingly
        s = 0                                  # Thus we can say , partially working like Method Overloading
        if a!=None and b!=None and c!=None:
            s = a+b+c

        elif a!=None and b!=None:
            s = a+b

        else:
            s = a

        return s

s2 = student1(60,98)
print(s2.m1)
print(s2.m2)
print(s2.sum(2,3,4))
print(s2.sum(2,3))
print(s2.sum(2))

print()