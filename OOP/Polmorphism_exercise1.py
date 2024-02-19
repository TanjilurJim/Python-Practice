class Cat():
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def info(self):
        print(f"The cat's name is {self.name} and it is {self.age} years old")

    def make_sound(self):
        print("Meaw, Meaw !!!!")

class Dog(Cat):
    def __init__(self,name,age):

        super().__init__(name,age)

    def info(self):
        print(f"The dog's name is {self.name}, it is {self.age} years old")

    def make_sound(self):
        print("Woof, Woof!!!!")


def my_pet(pet):
    pet.info()
    pet.make_sound()

c = Cat("rocky",3)
d = Dog("Kalu",2)

my_pet(c)
my_pet(d)


