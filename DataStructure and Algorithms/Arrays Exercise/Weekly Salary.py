# Weekly working hours given in a list. find weekly salary.
#take list of working hours as an input. take wage per hour as an input too

def weekly_salary(working_hours, wage_per_hour):
    total_hours = sum(working_hours)
    salary = total_hours * wage_per_hour
    return salary

num_of_days = int(input("Please enter the days you have worked :"))

hours_worked = []

for i in range(num_of_days):
    working_hours = float(input(f"Enter the amount of hours worked for day {i+1}"))
    hours_worked.append(working_hours)

wage_per_hour = float(input("Enter your wage per hour: "))

salary = weekly_salary(hours_worked, wage_per_hour)

print(f"Total weekly salary: ${salary}")
