#using loops number of digits in a number

n = int(input("please enter a number: "))

counter = 0
while n>0:
    n = n//10
    counter+=1


print(counter)




