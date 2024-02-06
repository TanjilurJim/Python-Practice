def max3(a,b,c):

    if a > b:
        max = a
    else:
        max = b

    if max < c:
        max = c

    return max

inputs=[]
for i in range(3):
    number = int(input(f"Please enter the {i+1} number"))
    inputs.append(number)

maximum = max3(*inputs)

print(maximum)

