g = 10

def fun1(a,b):
    c = a+b
    print('local variable is',c)
    print('global variable is', g)

fun1(4,8)
# global variable should be called before the function call