import Student, pickle

studs = [Student.student(10,'John','cs'),Student.student(30,'mike','ece')]

with open('students.data', 'wb') as f:
    for s in studs:
        pickle.dump(s,f)
