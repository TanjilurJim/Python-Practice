import csv

field_names = ["name",'Author','Publisher','Price','Category']
book1=['Computer Programming part 1','Tamim Shahriar subeen,','Onnorokom Prokashoni','200.00','Programming']
book2=['Computer Programming part 2','Tamim Shahriar subeen,','Dimik Prokashoni','250.00','Programming']

book_list = [book1,book2]

with open('books.csv','w') as csvf:
    csv_writer = csv.writer(csvf, delimiter=",",quotechar="\"",quoting = csv.QUOTE_MINIMAL)
    csv_writer.writerow(field_names)
    for book in book_list:
        csv_writer.writerow(book)


