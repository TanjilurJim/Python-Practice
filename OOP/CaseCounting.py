def countCase(phrase):
    upper= 0
    lower = 0

    for i in phrase:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1

    return upper,lower

str = input("please enter a string")

print(countCase(str))





