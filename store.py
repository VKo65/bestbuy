
from products import Product

class Store:
    """Constructor for class Store. """

    def __init__(self, products):
        self.list_of_products = products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        if product in self.list_of_products:
            self.list_of_products.remove(product)

    def get_total_quantity(self):
        return sum(product.quantity for product in self.list_of_products)

    def get_all_products(self):
        return [product for product in self.list_of_products if product.quantity > 0]

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product.quantity >= quantity:
                total_price += product.price * quantity
                product.quantity -= quantity  # Bestand reduzieren
            else:
                raise ValueError(f"Not enough quantity of {product.name}.")
        return total_price

def main():

    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))



if __name__ == "__main__":
    main()

