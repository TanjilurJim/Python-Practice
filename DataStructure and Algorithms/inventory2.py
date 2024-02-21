inventory = {"Apple": 200,"orange": 300,"Banan": 100}


def get_order_from_customer():
    # Initialize an empty dictionary for the order
    orders = {}

    while True:
        # Ask the customer for the item they want to order
        item = input("What would you like to order? (type 'done' to finish ordering): ")
        if item.lower() == 'done':  # Check if the customer is finished ordering
            break

        # Ask for the quantity of the item
        try:
            quantity = int(input(f"How many {item}(s) would you like? "))
        except ValueError:
            print("Please enter a valid number for the quantity.")
            continue  # Skip the rest of this iteration and ask for the next item

        # Capitalize the item to match the inventory format and add to the order
        item = item.capitalize()
        orders[item] = quantity

    return orders


def inventory_update(orders):
    for item, quantity in orders.items():
        if item in inventory and inventory[item] >= quantity:
            inventory[item] -= quantity
            print(f'Ordered {quantity} {item}(s).')
        else:
            print(f'Sorry, {item}(s) not available or insufficient quantity.')

    return inventory


# Inventory example
inventory = {"Apple": 200, "Orange": 300, "Banana": 100}

# Get the order from the customer
customer_order = get_order_from_customer()

# Update the inventory based on the customer's order
updated_inventory = inventory_update(customer_order)

print("Updated inventory:", updated_inventory)
