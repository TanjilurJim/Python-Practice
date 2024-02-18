class Course:
    def __init__(self,name,duration,*books):
        self.course_name = name
        self.course_duration = duration
        self.books = [self.Book(b) for b in books]

    def show_details(self):
        print('course name :', self.course_name)
        print('duration:', self.course_duration)
        print('suggested books:')
        for b in self.books:
            print(b.title)


    class Book:
        def __init__(self,title):
            self.title = title


        # def __str__(self):
        #     return self.title


c1 = Course('Python',10,'Learn python','Python Crash course','another books')
c1.show_details()
