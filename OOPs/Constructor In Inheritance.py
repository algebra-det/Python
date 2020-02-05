class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 is working of class a")

    def feature2(self):
        print("Feature 2 is working of class a")

class B(A) : #Single Level Inheritance

    def feature1(self):
        print("Feature 1 is working of class b")

    def feature4(self):
        print("Feature 4 is working of class b")

class C(A):
    def __init__(self):
        print("IN C init")
    def feature5(self):
        print("Feature 5 is working of class c")

print("For a1")
a1 = A()                # it will go to __init__ of class A
a1.feature1()

print("For b1")
b1 = B()                # it will also go to __init__ of class A as we don't have a constructor in class B
b1.feature1()

print("For c1")
c1 = C()                # it will go to __init__ of class C as we have init in class A , hence it won't go to class A
c1.feature2()
c1.feature5()
""" When we create an object of any class first it will search for __init__ of it's own class
    if not found it will go to parent/super class """

# We can also call the __init__ of super class by using super() function
class D:

    def feature6(self):
        print("Feature 6 is working of class D")

print("For d1")
d1 = D()
d1.feature6()

class E(D,B):                       # Try (B,D) ,  MRO (Method Resolution Order)
    def __init__(self):
        super().__init__()          # This will only call the init of A not B, as A is the first one from left to right
        print("In E init")          # It Uses MRO (Method Resolution Order) hence going in order from left to right
    def feature7(self):
        print("Feature 7 is working of class E")

    def feat(self):
        super().feature2()

print("For e1")
e1 = E()
e1.feature7()
e1.feat()
e1.feature1()                       # Same it will call feature1() of A not B , according to MRO
                                    # Try changing from E(A,B) to E(B,A)






