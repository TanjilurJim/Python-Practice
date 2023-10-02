n = int(input("please enter the number for factorial"))

factorial = 1
for i in range(n,1,-1):
    factorial = i*factorial


print(factorial)