class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} — {self.price} грн, на складі: {self.quantity} шт."

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, amount):
        if amount <= product.quantity:
            self.items.append((product, amount))
            product.quantity -= amount
            print(f"Додано {amount} шт. {product.name} до кошика")
        else:
            print(f"Недостатньо {product.name} на складі")

    def show_cart(self):
        print("\nКошик:")
        for product, amount in self.items:
            print(f"{product.name} — {amount} шт. ({product.price} грн/шт.)")
        total = sum(product.price * amount for product, amount in self.items)
        print(f"Загальна вартість: {total} грн\n")

# Приклад використання
p1 = Product("Ноутбук", 15000, 3)
p2 = Product("Миша", 500, 10)

cart = Cart()
cart.add_product(p1, 1)
cart.add_product(p2, 2)