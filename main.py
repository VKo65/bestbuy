import products
import store
# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start():
    print("\n  store Menu \n  ----------\n1. List all products in store\n"
          "2. Show total amount in store\n3. Make an order\n4. Quit")
    users_choice = input("Please choose a number: ")
start()



