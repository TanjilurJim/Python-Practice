n =int(input("please enter a number: "))

while n> 0:
    remainder = n%10
    n = n//10
    print(remainder)