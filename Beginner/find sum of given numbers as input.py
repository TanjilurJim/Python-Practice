#Ask user how many numbers he will give as input like 10, 11, 456,783 etc.
#then find sum of these inputs

num = int(input("how many inputs will you give"))
sum = 0
count = 0
while count < num:
    n = int(input("please enter a number:"))
    sum = sum+n
    count = count+1


print("sum is",sum)
print(count)




