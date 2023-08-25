def add(n1):
    return  n1+n1+n1

result = 0
for i in range(0,3):
    x = input("please insert a number")
    x = int(x)
    result = add(x)

print(result)


