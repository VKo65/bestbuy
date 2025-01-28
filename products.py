class Product:

    def __init__(self, name: str, price: float, quantity: int):
        """Constructor for product attributes with type and value checks. --> Shahriar"""
        # Type checks
        if not isinstance(name, str):
            raise TypeError("Product name must be a string.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number (int or float).")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")

        # Value checks
        if not name.strip():
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price must be non-negative.")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        # Assign to instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Default value for active status


    def get_quantity(self: float):
        """Just output of instance quality"""
        return self.quantity


    def set_quantity(self, quantity):
        """Function to be reduce quantity
        """
        self.quantity -= quantity
        if quantity < 1:
            deactivate()
        return


    def is_active(self):
        """Bool to check status of product"""
        return self.active


    def activate(self):
        """Function to activate product"""
        self.active = True
        return


    def deactivate(self):
        """Function to deactivate product"""
        self.active = False
        return


    def show(self):
        """Function to print information of the object """
        print(f"{self.name}, {self.price}, {self.quantity}")

    def buy(self, quantity: int):
        """Allows buying a specified quantity with type and value checks. --> Shahriar"""
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if quantity > self.quantity:
            raise ValueError(f"Not enough quantity in store. Available quantity: {self.quantity}.")

        self.set_quantity(quantity)  # Reduces quantity and deactivates if stock < 1
        return f"Total price is: {self.price * quantity:.2f}"


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