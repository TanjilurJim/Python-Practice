#the program will take one input and create 4 strings from it
#1st string will have only capital letters
#2nd will consist lowercase
#3rd will consist digits
#4th one will consist the rest
#i.e input: Hello, Test ! 123 123, good.
# output: 1. HT , 2. elloestgood 3.123123 !,.


def separate_strings(input_str):
    capitals = ""
    lowercase = ""
    digits = ""
    others = ""

    for char in input_str:
        if char.isupper():
            capitals += char
        elif char.islower():
            lowercase += char
        elif char.isdigit():
            digits += char
        else:
            others += char

    return capitals, lowercase, digits, others

input_str = input("Enter the string: ")

capitals, lowercase, digits, others = separate_strings(input_str)

print("1. " + capitals)
print("2. " + lowercase)
print("3. " + digits)
print("4. " + others)

