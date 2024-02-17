class Customer():

    def __init__(self, id, name,bdno,bdstreet,bcity,bcountry,bpin,sdno,sstreet,scity,scountry,spin):

        self.custid = id
        self.name = name
        self.baddrd = self.Address(bdno,bdstreet,bcity,bcountry,bpin)
        self.saddre = self.Address(sdno,sstreet,scity,scountry,spin)


    class Address():
        def __init__(self,dno, street, city, country,pin):
            self.deno =dno
            self.street = street
            self.city =city
            self.country = country
            self.pin = pin

        def display(self):
            print(self.deno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)



            
c =Customer(10,'john',101,'abc','dhaka','bd',10001,200,'ijk','lalbagh','bd',40001)
c.baddrd.display()

c.saddre.display()