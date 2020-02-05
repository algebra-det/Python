class car:

    wheels = 4                              # class variable which belongs to class namespace
                                            # without self the variable is class variable

    def __init__(self):                     # with self the variable is instance
        self.milege = 10                    # instance variable which belongs to instance/object namespace
        self.company = "BMW"                # instance variable which belongs to instance/object namespaec

"""
    THE VARIBALES WHICH ARE IN __INIT__ ARE INSTANCE VARIABLES
    AND VARIBALES WHICH ARE NOT IN __INIT__ ARE CLASS VARIABLES
    NAMESPACE: IT'S AN AREA WHERE YOU CREATE AND STORE OBJECT/VARIABLE
    - CLASS NAMESPACE
    - OBJECT/INSTANCE NAMESPACE
"""

car1 = car()
car2 = car()
car3 = car()

print("1.Company = ",car1.company," with Milege",car1.milege,"and wheels ",car1.wheels)
print("Company = ",car2.company,"with Milege",car2.milege,"and wheels ",car2.wheels)
print("Company = ",car3.company,"with Milege",car3.milege,"and wheels ",car3.wheels)

print()

car1.milege = 8
print("2.Company = ",car1.company," with Milege",car1.milege,"and wheels ",car1.wheels)
print("Company = ",car2.company,"with Milege",car2.milege,"and wheels ",car2.wheels)
print("Company = ",car3.company,"with Milege",car3.milege,"and wheels ",car3.wheels)

print()


car.wheels = 7
print("3.Company = ",car1.company," with Milege",car1.milege,"and wheels ",car1.wheels)
print("Company = ",car2.company,"with Milege",car2.milege,"and wheels ",car2.wheels)
print("Company = ",car3.company,"with Milege",car3.milege,"and wheels ",car3.wheels)

print()

car1.wheels = 6
print("4.Company = ",car1.company," with Milege",car1.milege,"and wheels ",car1.wheels)
print("Company = ",car2.company,"with Milege",car2.milege,"and wheels ",car2.wheels)
print("Company = ",car3.company,"with Milege",car3.milege,"and wheels ",car3.wheels)

print()

car.wheels = 9
print("5.Company = ",car1.company," with Milege",car1.milege,"and wheels ",car1.wheels)
print("Company = ",car2.company,"with Milege",car2.milege,"and wheels ",car2.wheels)
print("Company = ",car3.company,"with Milege",car3.milege,"and wheels ",car3.wheels)
