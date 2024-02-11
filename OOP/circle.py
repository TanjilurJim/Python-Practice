class Circle():

    pi = 3.1416

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
              
              return self.radius*self.radius*Circle.pi
    
    def parameter(self):
          return 2*self.pi*self.radius
    

myCircle = Circle(radius=4)
print('Area',myCircle.area())
print('parameter of the circle is',myCircle.parameter() )