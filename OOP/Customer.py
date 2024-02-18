class Customer:
    customer_no = 1
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.customer_no = Customer.customer_no
        Customer.customer_no += 1

    @classmethod
    def Customer_count(cls):
        return f'total customer: {cls.Customer_count}'

    def get_name(self):
        return self.name
    
    def get_phoneno(self):
        return self.phone
    
    def set_phoneno(self,no):
        self.phone = no

    def details(self):
        s =f"Name: {self.name}\n"
        s += f"Phone: {self.phone}\n"
        s += f'Customer no: {self.customer_no} \n'

        with open("customer.txt",'a+') as f:
            f.write(s)

        return s
    
c1 = Customer('Jim','01521584092')
print(c1.get_name())
print(c1.get_phoneno())

print(c1.set_phoneno('01791557014'))

print(c1.details())

c2 = Customer('Jim2','01521584092')
print(c2.get_name())
print(c2.get_phoneno())

# print(c2.set_phoneno('01791557014'))

print(c2.details())

# with open('customer.txt','r') as f:
#     content = f.read()
#     print(content)





    



