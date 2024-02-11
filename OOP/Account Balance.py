class AccountBalanceException(Exception):
    pass
class NegativeBalanceException(Exception):
    pass


balance = 10000

def withdraw(amt):
    global balance
    if amt < 0:
        raise NegativeBalanceException("The amount to withdraw cannot be negative.")

    elif balance - amt < 5000:
        raise AccountBalanceException(f'minimum balance should be {balance}')
    else:
        balance = balance - amt
        print(f'Remaining balance is {balance}')


try:
    amount = float(input("Enter the balance you want to withdraw: "))
    withdraw(amount)
except AccountBalanceException as e:
    print(f'error {e}')
except NegativeBalanceException as e:
    print(f"error {e}")



