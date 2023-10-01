import random

n = random.randint(1,10)

guess = 0

while guess != n :

    guess = int(input("Enter a number: "))

    if guess < n:
        print("The number you guessed is lesser")

    elif guess >n:
        print(" The number you guessed is larger")
    else:
        print("Yes you got the number")