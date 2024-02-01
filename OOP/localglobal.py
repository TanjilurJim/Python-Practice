g = 10

# def fun1(a,b):
#     c = a+b
#     print('local variable is', c)
#     print('global variable is', g)
#
#
# # global variable should be called before the function call
#
# def fun2():
#     print(g*2)
#
# fun1(4,8)
# fun2()

# def func():
#     g=20
#     print(g)
#
# func()
# print(g)

# the output shows the access of global and local variable
# A function can not modify global variables
# to modify need to use the keyword 'global'

# def fun1():
#     global g
#     g = g+5
#     print('global',g)
#
# fun1()
# print(g)

a,b,c,d = 11,22,33,44

def fun1(a=15,b=25):
    x,y,z = 1,2,3
    print(locals())

fun1()

print(globals())