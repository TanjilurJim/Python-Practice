from collections import deque
customers = deque()

def walk_in(customer):
    customers.append(customer)
    for i in customer:
        print(i, 'just walked in')

def serviced():
     cust = customers.popleft()
     print(f'{cust} customer leaves after a good trim')
     print('-----------------')

try:
    n = int(input("How many customers should take service?: "))
except ValueError as e:
    print("Error:", e)
    exit(1)

for i in range(1, n + 1):
    suffix = "st" if i == 1 else "nd" if i == 2 else "th"  # Generating correct ordinal suffix
    person = input(f"Name of the {i}{suffix} person: ")
    customers.append(person)

print(customers)

walk_in(customers)  # Pass the list of customers as an argument
serviced()
serviced()

print("in line", customers)