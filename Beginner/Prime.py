#if a number is divisible by itself and one and no other numbers. it is
#a prime number

n= int(input("Please enter a number: "))

count = 0

factors = []

for i in range(1,n+1):
    if n%i == 0:
        factors.append(i)
        count+=1

if count == 2:
    print("It's a prime number")


else:
    print("It's not a prime number. The factors are", factors)
