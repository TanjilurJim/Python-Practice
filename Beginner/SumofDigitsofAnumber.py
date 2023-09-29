#finding sum of the digits given as input and also printing the numbers in reverse

n = int(input("please enter a number: "))
print("the input you gave: ",n)
sum = 0
numbers = []
while n>0:
    r = n % 10
    n = n//10

    sum = sum + r
    numbers.append(r)


print("the sum is: ", sum)

print(numbers)


