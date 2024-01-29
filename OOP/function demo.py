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
#default should be on the rhs

def add(a,b=0,c=0):
    return a + b + c

print(add(10,b=5)) #first positional arg then keyword arg
