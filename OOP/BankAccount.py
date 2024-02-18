class MinimumBalanceError(Exception):
    pass

class Account():
    account_number = 1001
    def __init__(self,name,balance=1000):

        if balance < 1000:
            raise MinimumBalanceError("Account Cannot be Created")



        self.name = name
        self.account_number = Account.account_number
        Account.account_number +=1
        self.balance = balance



    def deposit(self,amount):
        self.balance +=amount


    def withdraw(self,amount):
        if self.balance - amount < 1000:
            raise MinimumBalanceError("Amount Cannot be withdrawn")
        self.balance -= amount


    def show_details(self):
        s = f'name: {self.name} \n'
        s += f'account_number: {self.account_number} \n'
        s += f'balance: {self.balance}'

        return s

# Attempt to create account a1
try:
    a1 = Account('John', 2000)
    print(a1.show_details())
    print('')
except MinimumBalanceError as e:
    print(e)

# Attempt to create account a2
try:
    a2 = Account('Jim', 500)  # This will raise MinimumBalanceError
except MinimumBalanceError as e:
    print(e)

# Attempt to create account a3
try:
    a3 = Account('Meem', 100020)  # This should succeed
    print(a3.show_details())
except MinimumBalanceError as e:
    print(e)

# Proceed with further operations on a1
try:
    a1.deposit(500)
    print(f'after the deposit \n',a1.show_details())
    a1.withdraw(2200)
    print(a1.show_details())
except MinimumBalanceError as e:
    print(e)





