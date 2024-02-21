from collections import Counter

price = {"Soap": 50, "Toothpaste": 20,"Shampoo":45.5,"Brush":15.99}

def generate_bill(cart):
    total = 0
    for item,qty in cart.items():
        print(item,':',price[item],'x',qty,"=",price[item]*qty)

        total += price[item] *qty

    print(total, "is the total bill")






cart = Counter()

while True:
    user_input = input("Enter the item you need. write no otherwise").capitalize()
    if user_input=="No":
        break
    else:
        if user_input in price:
            amount = int(input(f"How many {user_input} you need?"))


            cart[user_input] += amount
        else:
            print("Not Available")


generate_bill(cart)















