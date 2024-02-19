class Orders:
    orders_count = 0
    def __init__(self):
        self.cart = []
        self.items_count = Orders.items_count
        Orders.items_count += 1

    @classmethod
    def count(cls):
        return cls.items_count
    def add_to_cart(self,item):
        self.cart.append(item)



    def remove_from_cart(self,item):
        self.cart.remove(item)

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        items= 'Cart Contents: '
        for i in self.cart:
            items += i + ', '
        return items

o = Orders()
o.add_to_cart('Soup')
o.add_to_cart('Brush')
o.add_to_cart('Paste')

print('Cart Size:', len(o))
print(o)
print(o.count())


