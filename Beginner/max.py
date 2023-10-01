n = int(input("how many numbers you want to enter: "))

max = 0

for i in range(n):
    x = int(input("please enter a number : "))
    if x > max:
        max = x


print(max,"is the maximum number")





