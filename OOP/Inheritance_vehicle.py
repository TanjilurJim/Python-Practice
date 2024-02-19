class Vehicle:
    """Base class for all vehicles"""

    def __init__(self,name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turning", self.name,'to',direction)

    def brake(self):
        print(self.name, "is stopping")


class Car(Vehicle):
    """Car Class"""
    def __init__(self,name, manufacturer, color):
        self.year = 2017
        super().__init__(name,manufacturer,color)

        self.wheels = 4

        print(self.name,'manufactured byt',self.manufacturer , 'was built in', self.year, 'it has', self.wheels,'wheels')

    def change_gear(self, gear_name):
        """Method for changing gear """
        print(self.name, "is changin gear to", gear_name)

    def turn(self, direction):
        print(self.name,"is turning", direction)

if __name__ == "__main__":
    v1 = Vehicle('Fusion 110 Ex', 'walton','black')
    v2 = Vehicle('Softail Delux','Harley-Davidson','Blue')
    v3 = Vehicle('Mustang 5.0 GT Coupe','ford','Red')
    c = Car('Mustang 5.0 GT Coupe','ford','Red')

    v1.drive()
    print()
    v2.drive()
    print()
    # v3.drive()
    # print()
    c.drive()
    c.brake()
    c.change_gear("p")

    v1.turn("left")
    print()
    v2.turn('right')
    c.turn('straight')

    v1.brake()
    v2.brake()
    c.brake()
    # v3.brake()




