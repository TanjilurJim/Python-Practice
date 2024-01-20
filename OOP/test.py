class Student:
    'This is version 1.0'
    def __init__(self,roll,name,dept):
        self.roll = roll
        self.name = name
        self.dept = dept

    def __str__(self):
        return 'This is student class'

    def display(self):
        print('Student Name:', self.name)
        print('Roll number:', self.roll)
        print('Dept:', self.dept)



    # def display(self):
    #     print(f'Roll:{self.roll} \nName: {self.name}\nDept: {self.dept} ')

# instead of creating 3 reference variables we can create list of variables

S = [Student(101,'jim','cse'),Student(201,'abir','eee'),Student(303,'meem','arts')]

# S = Student(101,'jim','cse')
# S2 = Student(202,'abir','bba')

# print(S.roll)
# print(S.dept)
#
# print(S.__doc__)
# print(S)
# S.display()
# S2.display()

for i in S:
    i.display()