# def myfnc(x,z, y =10):
#     print("x=", x, "y=",y, "Z=", z)
#
#
# x = 5
# y = 6
#
#
# myfnc(x,y,z)
# myfnc(x,y)


# def add_numbers(numbers):
#     result = 0
#     for number in numbers:
#         result += number
#     return result
#
# result = add_numbers([1,2,3,4,45,6,9])
# print(result)


def test_fnc(li):
    li[0] = 10

my_list = [1,2,3,4]
print("before function call", my_list)
test_fnc(my_list)                                ##how to send list in a fucntion
print("after function call", my_list)

#to sum all the elements of the list

li = [1,2,3]
result = sum(li)
print(result)



