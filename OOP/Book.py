class Book():

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        return f'The book {self.title} is written by {self.author} and its price is {self.price} '
    

b = Book('50 shades of grey','Asim',200)
print(b.show_details())


    