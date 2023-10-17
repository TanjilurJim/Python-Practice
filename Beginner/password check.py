pass1 = input("please enter password: ")
pass2 = input("confirm password: ")

if pass1 == pass2:
    print("Confirmed")
else:
    if pass1.casefold() == pass2.casefold():
        print("Please check for cases and try again")
    else:
        print("Not matching try again")




