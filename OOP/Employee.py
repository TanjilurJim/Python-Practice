# class Employee():
#     employee_count = 101

#     def __init__(self,name,salary,designation):
#         self.name = name
#         self.salary = salary
#         self.designation =designation
#         self.emp_id ='e'+ str(Employee.employee_count) #because class variable
#         Employee.employee_count +=1



    
#     def show_details(self):
#         print('Name:', self.name)
#         print('id: ',self.emp_id)
#         print('Designation:', self.designation)
#         print('Salary:', self.salary)

#     @classmethod #because taking class variable
#     def total_employees(cls):

#         return f'total employees  {cls.employee_count - 101}'
    


    

# e1 = Employee('john',18000,'Manager')
# e2 = Employee('jim', 50000,'WebDev')

# e1.show_details()
# print(e1.total_employees())
# print('')
# e2.show_details()

class Employee():
    employee_count = 101

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.emp_id = 'e' + str(Employee.employee_count)  # because class variable
        Employee.employee_count += 1

    def show_details(self):
        details = f'Name: {self.name}\n'
        details += f'id: {self.emp_id}\n'
        details += f'Designation: {self.designation}\n'
        details += f'Salary: {self.salary}\n'
        return details

    @classmethod
    def total_employees(cls):
        return f'total employees: {cls.employee_count - 101}'
    @staticmethod
    def save_employee_details(employee_list, filename):
        with open(filename, 'w') as file:
            for employee in employee_list:
                file.write(employee.show_details() + '\n')
                file.write(employee.total_employees() + '\n\n')

e1 = Employee('john', 18000, 'Manager')
e2 = Employee('jim', 50000, 'WebDev')

# Save details to a text file
Employee.save_employee_details([e1, e2], 'employees.txt')
