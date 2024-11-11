class Product:
    """A class representing a generic product"""

    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self._category = category

    def restock(self, amount):
        """Increase the quantity of an item"""
        if amount > 0:
            self.quantity += amount
            print(f"{amount} units added!")
        else:
            print("Invalid amount!")

    def sell(self, amount):
        """Reduce quantity of items"""
        if 0<amount<=self.quantity:
            self.quantity -= amount
            print(f"{amount} units sold!")
        else:
            print("Not enough products")

    def display_info(self):
        """Displaying prducts"""
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")


def display_menu():
    """displays the main menu"""
    print("\n Menu: ")
    print("1. View Products")
    print("2. Add Products")
    print("3. Restock Product")
    print("4. Sell Product")
    print("5. Exit")

def view_products(products):
    if not products:
        print("NO product")
    else:
        for product in products:
            product.display_info()

products = []

product1 = Product("Pen", "$10", 10, "Stationary")
products.append(product1)
product1.restock(500)
product1.sell(300)
# product1.display_info()

while True:
    display_menu()
    choice = input("Enter your choice [1-5]: ")

    if choice == "1":
        view_products(products)
