class computers:
    """ Just like we used __name__ special variable previously , here we will use special method
    which will be used to define two variables in a class"""

    def __init__(self):                     # this will be called automatically
        print("in it")

    def config(self):                       # It will be called manually like below in com1.config()
        print("i5 with 8 gb ram")



com1 = computers()                          # init will be called automatically
com2 = computers()                          # init will be called automatically

com1.config()                               # manually called config

print()

class computers1:
    def __init__(self,cpu,ram):             # self here is the object itself
        self.cpu = cpu
        self.ram = ram

    def config1(self):
        print("hello config is ",self.cpu , self.ram)


com3 = computers1("i3","16")                # here we are passing 3 arguments to __init__ , 1 is com3,2 is i3 cpu,and 3 is 16 ram
com4 = computers1("i7","32")

com3.config1()
com4.config1()