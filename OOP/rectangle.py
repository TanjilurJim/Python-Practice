class Rectangle():

    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def area(self):
        return self.length * self.breadth
    
    @staticmethod
    def issquare(lent,bre):
        return lent ==bre
    

r1 = Rectangle(10,5)

print(r1.issquare(10,10))