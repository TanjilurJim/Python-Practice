#if user gives a number it will create its table otherwise it will provide multiplication table for 1.

def mul_table(n=1):
    for i in range(1,11):
        print(n,"x",i, "=", n*i)

number = input("Enter a number for its multiplication table")

if number.isdigit():
    mul_table(number)
else:
    print("You didn't input any number:")
    mul_table()



