class camera:

    cables = 5

    def __init__(self):
        x = input("\nEnter the camera's brand name ")
        self.brand = x
        z = int(input("Enter the camera's power"))
        self.power = z
        self.area = self.area()

    def cable(self):
        self.totalpower =  self.power*self.cables

    def show(self):
        self.cable()
        print("\nBrand -",self.brand,",Power -",self.power, ",Cable -",self.cables,",Total Power -",self.totalpower,end=",")
        self.area.show()

    class area:

        def __init__(self):
            self.areas = "Yadav Colony"
            self.colony = 65

        def show(self):
            print(" Area-",self.areas,",Colony Code -",self.colony)


camera1 = camera()
camera1.show()
camera2 = camera()
camera2.show()

print()

camera.cables = 8
camera2.show()
print()

camera1.area.areas = "mcf"
camera1.area.show()
cam2 = camera2.area
cam2.colony = 98
cam2.show()