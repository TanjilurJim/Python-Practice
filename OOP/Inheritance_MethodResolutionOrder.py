class A:
    def show(self):
        print('A')

class B(A):
    pass
    # def show(self):
    #     print('B')

class C(B):
    pass


# b =B()
# b.show()

# print(B.mro())
c = C()
c.show()
