class Car:
    # name = ""
    # color = ""

    def __init__(self,n,c):
        self.name = n
        self.color = c


    def start(self):
        print("Starting the engine")

my_car = Car("Allion", "White")
# my_car.name = "Allion"
# my_car.color = "Blue"

print(my_car.name)
print(my_car.color)
my_car.start()