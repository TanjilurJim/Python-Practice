# class Student():

#     section = 'Galaxy' #class object attribute

#     def __init__(self,name,gpa):

#         self.name = name
#         self.gpa = gpa

# stu1 = Student(name='Jim',gpa=4.0)
# stu2 = Student(name = 'Mimi',gpa=3.7)



        


# print(stu1.name,f'from {stu1.section} your gpa is :', stu1.gpa)

class Agent():

    origin = "USA"

    def __init__(self, name, height, weight):
        self.name = name    
        self.height = height    
        self.weight = weight    


x = Agent('Jose',24,170)



print(x.name,x.height,x.weight,x.origin)