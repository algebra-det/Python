
class computers:

    def config(self):
        print("this is an i5 machince and 1tb rom")

a = 5                           # a is our object of class int
com1 = computers()              # com1 is our object of class computers
com2 = computers()              # com2 is also our object of class computers

print(type(a))                  #Its class str, str is a built-in class
print(type(com1))               #its class computers , its our created class

# Simply calling the config() funciton will not work
# We can only call it by mentioning the class name too

"""
    computers.config() will also not work
    as here we have mentioned class with function but haven't defined for which object we want this function
    for example,
        you have mentioned class , and defined function which says 'walk' but we haven't defined
        which object means what attribute, as 'akash walk' or 'mickey walk' 
        that's why we have to mention the object too
    same way we have to state, class.function(object)
        in 'COMPUTERS' WE WANT 'CONFIGURATIONS' OF 'COMPUTER1'
            class                   config              com1

"""
int.bit_length(a)                   # its how we define class.method(object)
computers.config(com1)              # Our deined
computers.config(com2)
print()

# OR   In Short

a.bit_length()                      # here a will act as a parameter
com1.config()                       # Here com1 will be used a parameter without stating in the backets
com2.config()                       # this is also called another behaviour

