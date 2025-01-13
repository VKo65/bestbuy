class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """Constructor for product attributes"""
        if not name or not isinstance(name, str):
            raise Exception("Product name cannot be empty and must be string!")
        if price < 0:
            raise Exception ("Price must be positive!")
        if quantity < 0 or not isinstance(quantity, int):
            raise Exception("Quantity must be positive integer!")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self: float):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity -= quantity
        if quantity < 1:
            deactivate()
        return

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True
        return

    def deactivate(self):
        self.active = False
        return
    def show(self):
        print(f"{self.name}, {self.price}, {self.quantity}")

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception(f"There is not enough quantity in store. Available Quantity is: {self.quantity}")

        else:
            if self.quantity >= quantity:
                self.set_quantity(quantity)
                if self.quantity == 0:
                    self.active = False
            return f"Total price is: {self.price * quantity}"
def main():
    """bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()"""

if __name__ == "__main__":
    main()