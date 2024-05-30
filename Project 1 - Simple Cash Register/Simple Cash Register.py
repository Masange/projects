"""
Program Purpose        : Create a simple Cash Register.
Assignment #           : 11.1
Author                 : Kapambwe Chulu
Original Creation date : 2/23/2023
"""
import locale
locale.setlocale(locale.LC_ALL, '')


class CashRegister:
    items = []

    def __init__(self):
        self.count = 0.0
        self.total = 0.0

    @staticmethod
    def add_item(price):
        # This method keeps track of the items in the Cart.
        CashRegister.items.append(price)
        print(" ")
        print("Price: ", locale.currency(price, grouping=True))

    def get_count(self):
        # This method counts the number of items in the Cart.
        self.count = len(CashRegister.items)
        print("You now have " + str(self.count) + " items in your cart")

    def get_total(self):
        # This method calculates the total price of items in the Cart.
        self.total = sum(CashRegister.items)
        print("Your Total is currently ", locale.currency(self.total, grouping=True))


def main():
    """The main method prompts the user for the price of the item they wish to purchase  and calls other functions to
    calculate the number of items in the cart and the total price of items."""
    print(" Welcome to General store ")
    price = ''
    while price != 0:
        print(" ")
        try:
            price = float(input('Please enter a valid price to add an item to your cart or 0 to Quit:'))
        except ValueError:
            print("    Sorry , the value you entered is not a valid price.")
            continue
        if price == 0:
            print("***You Entered 0 to Quit. Thank you for visiting General Store. Hope you call again.*** ")
            break
        elif price > 0:
            register = CashRegister()
            register.add_item(price)
            register.get_count()
            register.get_total()
        else:
            print("    Sorry , the value you entered is not a valid price.")


if __name__ == '__main__':
    main()
else:
    # The statements below will execute if this program is imported to another module.
    print(" Note: You are using functions which were created in another module. ")
