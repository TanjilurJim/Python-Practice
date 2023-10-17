pass1 = input("please enter the password : ")


if len(pass1)>=8:
    last_digits =  pass1[-4:]
    asterisks = '*' * len(pass1)
    hidden_password = asterisks + last_digits

else:
    print("need atleaset 8 characters")

print(f"Your password is{hidden_password}")