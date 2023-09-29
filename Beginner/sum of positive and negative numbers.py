#from the given inputs will sum the positive and negatives

num = int(input("how many inputs will you give"))
sumOfPostivie = 0
sumOfNegative = 0
count = 0
while count < num:
    n = int(input("please enter a number:"))
    if n>0:
        sumOfPostivie = sumOfPostivie+n
    elif n<0:
        sumOfNegative = sumOfNegative +n
    else:
        print("It is 0 so we didn't count")

    count = count+1






print("sum of positive is",sumOfPostivie)
print("sum of negative is",sumOfNegative)
print(count)
