item = input("Enter the Item: ")
price = input("Enter the price: ")

total_len = len(item)+len(price)

# print(total_len)

dots = '.'*(25-total_len)

print(item, dots,price)
