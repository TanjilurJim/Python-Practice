# L = [10,20,30,431,23]
#
# try:
#     index = int(input('Enter index'))
#     print(L[index])
#     print('end of try block')
# except (IndexError, ValueError) as msg:
#     print(msg)
# # except ValueError:
# #     print('enter only integer value')
#
# print('Terminated Gracefully')



def div(a,b):
    if b != 0:
        res = a//b
        print(res)
    else:
        raise ZeroDivisionError

a = int(input('Enter the first number :'))
b =int(input("enter the 2nd number: "))

try:
    c = div(a,b)
    print(c)
except ZeroDivisionError as msg:
    print('ZeroDivsion error',msg)
