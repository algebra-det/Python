class a:
    def feature1(self):
        print("Feature 1 is working of class a")

    def feature2(self):
        print("Feature 2 is working of class a")

class b (a): #Single Level Inheritance
    def feature3(self):
        print("Feature 3 is working of class b")

    def feature4(self):
        print("Feature 4 is working of class b")

class c(b): #Multi Level Inheritance
    def feature5(self):
        print("Feature 5 is working of class c")

class d:
    def feature6(self):
        print("Feature 6 is working of class d")

class e(a,d): #Multiple Inheritance
    def feature7(self):
        print("Feature 7 is working of class e")

a1 = a()
print("In object a")
a1.feature1()
a1.feature2()

b1 = b()
print("In object b1")
b1.feature1()
b1.feature3()

c1 = c()
print("In object c1")
c1.feature2()
c1.feature5()

d1=d()
print("In object d1")
d1.feature6()

e1 = e()
print("In object e1")
e1.feature1()
e1.feature6()
e1.feature7()






