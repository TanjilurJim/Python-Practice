# def add3(a, b, c):

#     print(id(a), id(b),id(c))
#
# x,y,z = 10, 15, 5
#
# print(id(x),id(y),id(z))
#
# add3(x,y,z)
#
#   r = a+b+c
#   return a+b+c
# #
# # print(add3(10,15,5))
# #

# POSITIONAL vs KEYWORD ARGUMENTS

# def net_sal(basic, allowance, deduction):
#
#     net = basic + allowance -deduction
#
#     return net
#
# print("His net salary is,",net_sal(8000,6000,2000))
#
# n = net_sal(deduction=2000,basic=8000,allowance=6000) #keyword arg
#
#
#
# print(n)

# Default Arguments
#default arg should be on the rhs

# def add(a,b=0,c=0):
#     return a + b + c
#
# print(add(10,b=5)) #first positional arg then keyword arg

# Here we are not passing the list yet creating a list
# def additem(item,L=[]):
#
#     L.append(item)
#
#
#     return L
#
#
# # l1 = []
# n = int(input("please enter the amount"))
# for i in range(n):
#     x = int(input(f'Please enter{i}th integer'))
#     (additem(x))
#
# print(additem(1))

# def additem(item=None, L=[]):
#     if item is not None:
#         L.append(item)
#     return L
#
# n = int(input("Please enter the amount: "))
# for i in range(n):
#     x = int(input(f'Please enter {i+1}th integer: '))
#     additem(x)
#
# # Call the function without adding a new item
# print(additem())


#  MIXED POSTIONAL OR KEYWORD ARGS

# def add(a,b,c,d,e,f):
#     return a+b+c+d+e+f
#
# r = add(f=9,a=1,b=3,c=8,d=1,e=3)
# print(r)
#
# def add2(a,b,/,c,d,e,f):
#     print(a,b,c,d,e,f)
#     return a+b+c+d+e+f
#
# r = add2(2,5,f=9,c=8,d=1,e=3)
# print(r)
#
# def add3(a,b,/,c,d,*,e,f):
#     print(a,b,c,d,e,f)
#     return a+b+c+d+e+f
#
# s = add3(2,5,2,d=1,f=9,e=8)
# print(s)

#Variable Lenght Arguments
# def fun1(*args):
#     print(args)
#     print(type(args))
#
# l1 = [123,1]
#
# fun1(l1,120,123,'saf')

#unpacking Arguments

# def fun2(a,b,c):
#     print(a,b,c)

# l1 =[11,22,33]
# fun2(l1[0],l1[1],l1[1])
# but how can I pass the values of l1 distributed among a,b,c ?

# def fun2(a,b,c):
#      print(a,b,c)
#
# l1 = [11,22,33]
#
# fun2(*l1)

#Keyword Variable Length Arguments

# def func2(**kwargs):
#     for x in kwargs:
#         print(x,kwargs[x])
#
# func2(name='bob', roll=10, addr = 'Dhaka')

# Mixed arguements

# def func3 (a,b, *args, **kwargs):
#     print(a,b, args, kwargs)
#
# l1 = [12,312]
# func3(10,25,l1,1.5 ,c = 5)


def display():
    print("hello")

def fun(d):
    d()


fun(display)
