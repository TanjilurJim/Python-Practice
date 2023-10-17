pass1 = input("please enter password: ")
pass2 = input("confirm password: ")

if pass1 == pass2:
    print("Confirmed")
else:
    if pass1.casefold() == pass2.casefold():
        print("please check for cases and try again")
    else:
        print("not matching try again")




