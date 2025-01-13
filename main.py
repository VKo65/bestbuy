import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]


def start():
    """Get product list from Store.
    Output Store menu and prompt user to choose action.
    Execute with the methode from """
    best_buy = store.Store(product_list)
    print("\n  Store Menu \n  ----------\n1. List all products in store\n"
          "2. Show total amount in store\n3. Make an order\n4. Quit")
    users_choice = int(input("Please choose a number: "))
    if users_choice > 4:
        raise Exception("Store Menu has only 4 choices!")
    elif users_choice == 1:
        for product in best_buy.get_all_products():
            product.show()
    elif users_choice == 2:
        print(f"Total quantity in store: {best_buy.get_total_quantity()}")
    elif users_choice == 3:
        #for product in best_buy.get_all_products():
            #print(product.name)
        product_name = input("Please enter product name: ")
        try:
            product_quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Quantity should be a whole number!")
            return True

        # Search product name
        chosen_product = None
        for product in best_buy.get_all_products():
            if product.name == product_name:
                chosen_product = product
                break

        if chosen_product is None:
            print(f"Error: Product '{product_name}' not found!")
            return True

        # Create order list from users input
        order_list = [(chosen_product, product_quantity)]
        try:
            total_price = best_buy.order(order_list)
            print(f"Order successful! Total price: ${total_price:.2f}")
        except Exception as e:
            print(f"Order failed: {e}")
    elif users_choice == 4:
        print("Goodbye!")
        return False
    return True

def main():
    while start():
        pass

if __name__ == "__main__":
    main()

