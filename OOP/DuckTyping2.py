def PetLover(pet):
    pet.talk()
    if hasattr(pet, 'walk'):
        pet.walk()


class Duck:
    def talk(self):
        print("Duck is Talking")

    def walk(self):
        print("Duck is walking")

class Dog:
    def talk(self):
        print("Dog is Talking")

    # def walk(self):
    #     print("Dog is walking")

d = Duck()

PetLover(d)

doggy = Dog()
PetLover(doggy)


# def PetLover(pet, actions):
#     if "talk" in actions:
#         pet.talk()
#     if "walk" in actions and hasattr(pet, 'walk'):
#         pet.walk()

# class Duck:
#     def talk(self):
#         print("Duck is Talking")

#     def walk(self):
#         print("Duck is walking")

# class Dog:
#     def talk(self):
#         print("Dog is Talking")

#     # Uncomment to enable walking for Dog
#     # def walk(self):
#     #     print("Dog is walking")

# d = Duck()
# # To only talk
# PetLover(d, ["talk"])
# # To talk and walk
# PetLover(d, ["talk", "walk"])

# doggy = Dog()
# # To only talk
# PetLover(doggy, ["talk"])
# # If Dog class had a walk method and you wanted to both talk and walk
# # PetLover(doggy, ["talk", "walk"])