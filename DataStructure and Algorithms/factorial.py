# Task 1:
#
#
# Given an integer ‘n’, write a function
# to calculate the factorial of a given non-negative integer 'n'.
#




def factorial(n):
    if n<0:
        return "Please enter a non-negative number: "
    elif n ==0:
        return 1

    else:
        result =1
        for i in range(1, n+1):
            result *= i
        return result

try:
    n = int(input("please enter a non-negative integer for factoral calculation: "))
    print("Result: ",factorial(n))
except ValueError:
    print("That's not a vlid integer. Please enter a valid non-negative integer: ")
