from collections import Counter

inventory = Counter(apple = 50, banana =200,mango = 300,orange = 100)

order = {"apple": 10,'banana':20}

def update_inventory(order):
    inventory.subtract(order)


order = Counter(apple=10,banana =12, orange =5)

update_inventory(order)


print(inventory)