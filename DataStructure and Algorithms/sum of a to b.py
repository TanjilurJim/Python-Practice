# Task 2:
#
#
# A function to calculate the sum of all natural numbers
# between ‘a’ to  'b'.

def sumOfNaturalNumbers(a,b):

    # a = int(input("Please enter the lower bound number: "))
    # b = int(input("Please enter the upper bound number: "))
    sum = 0
    if a<b:
        for i in range(a,b+1):
            sum+=i
    else:
        for i in range(b,a+1):
            sum+=i
    return sum


a = int(input("Please enter lower bound number: "))
b = int(input("Please enter lower bound number: "))

print(sumOfNaturalNumbers(a,b))
