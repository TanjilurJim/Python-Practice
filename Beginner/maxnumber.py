n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = input("Enter the third number: ")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1>n2:
    max_num = n1
else:
    max_num = n2

if n3>max_num:
    max_num = n3

print("Maximum number is" , max_num )



