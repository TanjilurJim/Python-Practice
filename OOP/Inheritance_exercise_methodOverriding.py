import math
class Shape:
    """Parent class"""

    def __init__(self,name):
        self.name = name

    def area(self):
        return 'Shape area'


class Rectangle(Shape):

    def __init__(self,length,breadth,):
        self.length = length
        self.breadth =breadth


    def area(self):
        a = self.length * self.breadth
        return a


class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius

    def area(self):
        a = math.pi * self.radius**2
        return f'Area of Circle is {a}'


r = Rectangle(10,5)
print(r.area())
c= Circle(5)
print(c.area())

# s = Shape(10)
# print(s.area())


