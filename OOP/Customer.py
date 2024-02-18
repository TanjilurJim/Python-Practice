class Customer:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def get_name(self):
        return self.name
    
    def get_phoneno(self):
        return self.phone
    
    def set_phoneno(self,no):
        self.phone = no

    def details(self):
        s =f"Name: {self.name}\n"
        s += f"Phone: {self.phone}"

        with open("customer.txt",'w+') as f:
            f.write(s)

        return s
    
c1 = Customer('Jim','01521584092')
print(c1.get_name())
print(c1.get_phoneno())

print(c1.set_phoneno('01791557014'))

print(c1.details())

# with open('customer.txt','r') as f:
#     content = f.read()
#     print(content)





    



