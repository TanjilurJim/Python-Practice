s1 = input("please enter a string: ")

rev = s1[::-1]
if rev.casefold() != s1.casefold():

    print(s1,"It's a palindrome. Let's convert it")
    print(s1+rev)
else:
    print("it's already a palindrome")