class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id #private attribute
        self.__name = name #private attribute 
        self.__price = price #private attribute
        self.__stock = stock

    #getters
    def get_product_id(self):
        return self.__product_id
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_stock(self):
        return self.__stock
    
    #setters
    #setter for price and stock
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print(f"Price for {self.__name} is updated to: {self.__price}")
        else:
            print("Invalid price!")

    def set_stock(self, new_stock):
        if new_stock >= 0:
            self.__stock = new_stock
            print(f"Stock for {self.__name} is updated to: {self.__stock}")
        else:
            print("Invalid stock value!")

    #methods 
    def update_stock(self, quantity):
        if self.__stock + quantity >=0:
            self.__stock += quantity
            print(f"Stock for {self.__name} updated to {self.__stock}")
        else:
            print("Not enough stock to remove!")
    
    def calculate_value(self):
        return self.__price * self.__stock

class Inventory:
    def __init__(self):
        self.__products={} #private dict to store product

    def add_product(self, product):
        if product.get_product_id() in self.__products:
            print("Product already exist in inventory!")
        else:
            self.__products[product.get_product_id()] = product
            print(f"Product{product.get_name()} added to inventory")
    
    def update_product_price(self, product_id, new_price):
        if product_id in self.__products:
            self.__products[product_id].set_price(new_price)
        else:
            print("Product not found!")

    def update_product_stock(self, product_id, quantity):
        if product_id in self.__products:
            self.__products[product_id].update_stock(quantity)
        else:
            print("Product not found!")
    
    def view_inventory(self):
        print("\n--- Invenotry Report ---")
        for product in self.__products.values():
            print(f"ID: {product.get_product_id()}, Name: {product.get_name()}, "f"Price: {product.get_price()}, Stock: {product.get_stock()}, "
                  f"Value: {product.calculate_value():.2f}")
            print("--- End of Report ---\n")

    def calculate_total_inventory_value(self):
        total_value = sum(product.calculate_value() for product in self.__products.values())
        print(f"Total Inventory Value: {total_value:.2f}")

# Example Usage
# Creating the Inventory
store_inventory = Inventory()

# Adding Products
product1 = Product(1, "Laptop", 1000, 10)
product2 = Product(2, "Phone", 500, 20)
product3 = Product(3, "Headphones", 50, 100)

store_inventory.add_product(product1)
store_inventory.add_product(product2)
store_inventory.add_product(product3)

# Viewing Inventory
store_inventory.view_inventory()

# Updating Product Price and Stock
store_inventory.update_product_price(2, 550)  # Update Phone price
store_inventory.update_product_stock(3, -30)  # Remove 30 Headphones from stock

# Viewing Updated Inventory
store_inventory.view_inventory()

# Checking Total Inventory Value
store_inventory.calculate_total_inventory_value()