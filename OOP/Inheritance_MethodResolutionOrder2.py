# class A:
#     # def show(self):
#     #     print('A')
#     pass

# class B:
#     def show(self):
#         print('B')
#     # pass

# class C(A,B):
#     pass
#     # def show(self):
#     #     print('C')


# c = C()
# c.show()

# now what if C inherits from b and y where b inherits from a and y inherits from X

class A():
    def show(self):
        print('This is class A')


    
class B(A):
    pass

class X():
    def display(self):
        print('This is class X')
    pass
class Y(X):

    pass

class C(B,Y):
    pass




c = C()
c.show()
c.display()