#  5 x 1 =5

n = int(input("You want multiplication table of ? :"))

counter = 1
while counter<=10:
    result = n*counter
    print(n,"x",counter,"=", result )
    counter= counter+1

print("The multiplication table of", n)
