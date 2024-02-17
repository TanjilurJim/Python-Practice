class Rectangle():

    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def area(self):
        return self.length * self.breadth
    
    # @staticmethod
    # def issquare(lent,bre):
    #     return lent ==bre


class Cuboid(Rectangle):
    def __init__(self, length, breadth,h):
        self.height = h

        super().__init__(length, breadth)
    def volume(self):
        return self.length * self.breadth * self.height
    

    

# r1 = Rectangle(10,5)
# print(r1.area())
# print(r1.perimeter())

# print(r1.issquare(10,10)) 
    
c = Cuboid(10,5,3)

print(c.volume())