
def stage(age):
    try:
        if age<0:
            raise ValueError("Age cannot be negative.")



        elif age < 13:
            print(f'he is only {age} years old. He is a kid')
        elif age >= 13 and age <19:
            print(f'you are {age} hence you are a teen')
        elif age >19 and age <=50:
            print(f'you are {age} so still young')
        else:
            print(f'It is okay to be old. You are {age}')
    except ValueError as e:
        print(f"Error: {e} ")



try:
    age = int(input("Enter your age: "))
    stage(age)
except ValueError as e:
    print(f"Error: {e}")








