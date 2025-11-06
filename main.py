"""
Main program for managing a store's operations using a menu-driven interface.

This script facilitates various operations in a store, such as listing all
products, showing the total quantity of items, making orders, and exiting the
program. It uses objects like `Store`, `Menu`, and `MenuObject` to perform the
operations and to interact with the user.
"""

import sys
from typing import Callable

from store import Store
from products import Product
from menu import Menu, MenuObject

# menu items to create the cli menu with the Menu class
store_menu: MenuObject = MenuObject(
    menu_items=[
        'List all products in store',
        'show total amount in store',
        'Make an order',
        'Quit'
    ],
    header='Store Menu',
    seperator='----------',
    footer='Please choose a number: '
)

# Store inventory at the start
product_list: list[Product] = [
    Product(
        "MacBook Air M2",
        1450,
        100
    ),
    Product(
        "Bose QuietComfort Earbuds",
        250,
        500
    ),
    Product(
        "Google Pixel 7",
        500,
        250
    )
]


def list_products(store: Store) -> None:
    """
    Lists all the products available in the given store.

    :param store: A Store object containing the collection of products.
    :type store: Store
    """
    print(store.show_all())


def total_amount(store: Store) -> None:
    """
    Calculates the total amount of items present in the store and prints the result.

    :param store: Store object that provides the total quantity of items.
    :type store: Store
    """
    print(f"Total of {store.get_total_quantity()} items in store")


def make_order(store: Store) -> None:
    """
    Creates a shopping order based on user input and processes it through the provided store.

    The function interacts with the user in a loop to allow them to select products from
    the store, specify quantities, and build a shopping list. The user can end the
    process by entering an empty input. Once the shopping list is finalized, the total
    payment for the order is calculated using the store's ordering system and is displayed.

    :param store: An instance of the Store class used for managing products and processing orders.
    :type store: Store
    """
    shopping_list = []
    while True:
        print(store.show_all())
        print("When you want to finish order, enter empty text.")

        product = input("Which product # do you want? ")
        amount = input("Which amount do you want? ")

        if product == "" or amount == "":
            break

        elif not product.isdigit() or not amount.isdigit():
            print("error adding product")

        else:
            product = int(product)
            amount = int(amount)
            shopping_list.append((store.get_all_products()[product - 1], amount))
            print("Product added to list!")

    total = store.order(shopping_list)
    if total > 0:
        print(f"********\nOrder made! Total payment: ${total}")


def start(store: Store, menu: Menu) -> None:
    """
    Start the main application loop, allowing users to interact via a menu. Based on user
    input, it dispatches tasks like listing products, calculating total amounts, making
    orders, or exiting the application.

    The function relies on dispatcher mappings to route user input to appropriate
    functions. It runs continuously until the user explicitly chooses to exit.

    :param store: The Store instance containing available products and operations
        for managing inventory and orders.
    :type store: Store

    :param menu: The menu string presented to the user to guide their choices.
    :type menu: Menu
    """
    dispatcher: dict[str, Callable] = {
        '1': list_products,
        '2': total_amount,
        '3': make_order,
        '4': sys.exit
    }

    while True:
        user_choice = input(menu)

        if user_choice == '4':
            dispatcher.get(user_choice)()

        if user_choice in dispatcher:
            dispatcher.get(user_choice)(store)

        else:
            print("Error with your choice! Try again!")


def main() -> None:
    """
    Manages the main execution entry point of the application.

    This function initializes key components including the Store object and Menu
    object, leveraging provided configurations such as product list and store
    menu. It serves as the primary orchestration point for running the
    application logic, ensuring proper initialization and execution flow.
    """
    best_buy: Store = Store(product_list)
    menu: Menu = Menu(store_menu)

    start(best_buy, menu)


if __name__ == '__main__':
    main()
