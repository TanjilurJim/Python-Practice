n = int(input("please enter a number: "))

for i in range(n):
    for j in range(i+1,n):
        print("*",end="")

    print("")