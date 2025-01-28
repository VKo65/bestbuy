from products import Product


class Store:

    def __init__(self, product):
        """Constructor for store attributes with type and value checks. --> Shahriar"""
        if not isinstance(product, list):
            raise TypeError("Product list must be a list.")
        if not all(isinstance(item, Product) for item in product):
            raise TypeError("All items in the product list must be instances of the Product class.")
        if not product:
            raise ValueError("Product list cannot be empty.")

        self.list_of_products = product

    def add_product(self, product):
        """Adds a product to the store after type and value checks. --> Shahriar"""
        if not isinstance(product, Product):
            raise TypeError("The product to add must be an instance of the Product class.")
        self.list_of_products.append(product)

    def remove_product(self, product):
        """Removes a product from the store after type and value checks. --> Shahriar"""
        if not isinstance(product, Product):
            raise TypeError("The product to remove must be an instance of the Product class.")
        if product not in self.list_of_products:
            raise ValueError("The product to remove is not in the store.")
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        """Returns the total quantity of all products in the store. --> Shahriar"""
        if not self.list_of_products:
            raise ValueError("The product list is empty.")
        return sum(product.quantity for product in self.list_of_products)

    def get_all_products(self):
        """Generates a list of all available products"""
        return [product for product in self.list_of_products if product.quantity > 0]

    def order(self, shopping_list):
        """Function used in main, to order a created list (from user input).
        Check if quantity is available and calculate new quantity and total price.
        Return the total price, after type and value checks. --> Shahriar"""
        if not isinstance(shopping_list, list):
            raise TypeError("Shopping list must be a list of tuples (Product, quantity).")
        if not all(isinstance(item, tuple) and len(item) == 2 for item in shopping_list):
            raise TypeError("Each item in the shopping list must be a tuple (Product, quantity).")
        total_price = 0
        for product, quantity in shopping_list:

            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError(f"Invalid quantity: {quantity}. Quantity must be a positive integer.")

            if product.quantity >= quantity:
                total_price += product.price * quantity
                product.quantity -= quantity  # Reduce Quantity

            else:
                raise ValueError(f"Not enough quantity of {product.name}.")
        return total_price

def main():

   """ product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    oproducts = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(oproducts[0], 1), (oproducts[1], 2)]))"""



if __name__ == "__main__":
    main()

