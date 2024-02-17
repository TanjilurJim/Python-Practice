class Arith():
    def summation(self,a,b,c=None):
        s =a +b
        if c == None:
            return s
        else:
            return s+c
        

a = Arith()

print(a.summation(10,23.4))
print(a.summation(10,12,13))

 