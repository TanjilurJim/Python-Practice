class Student:
    def __init__(self,roll,name, dept):
        self.roll = roll
        self.name = name
        self.dept = dept

    def __str__(self):
        return 'This is student class'

    def display(self):
        print(f'Roll:{self.roll} \nName: {self.name}\nDept: {self.dept} ')

