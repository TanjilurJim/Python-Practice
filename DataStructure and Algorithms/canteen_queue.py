from collections import deque


"""Students are standing in the queue based on their roll number
so,if today in lunch roll 1 is served first
next day roll 2 will be served first and roll 1 will go back to the last of the line"""

students = deque([1,2,3,4,5,6,7,8])



def serve_food():

    print("Students are Served in Order:", students)
    students.rotate(-1)










print('Breakfast')
serve_food()
print("Lunch")
serve_food()




