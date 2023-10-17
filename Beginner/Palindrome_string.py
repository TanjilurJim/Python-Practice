s1 = input("please enter a string: ")

rev = s1[::-1]
if rev.casefold() == s1.casefold():

    print(s1,"It's a palindrome")
else:
    print("not a palindrome")