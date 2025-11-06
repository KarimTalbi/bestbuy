import sys
from store import Store
from products import Product
from menu import Menu, MenuObject

store_menu = MenuObject(
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

product_list = [
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


def list_products(store: Store):
    print(store.show_all())


def total_amount(store: Store):
    print(f"Total of {store.get_total_quantity()} items in store")


def make_order(store: Store):
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


def start(store: Store, menu: Menu):
    dispatcher = {
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


def main():
    best_buy = Store(product_list)
    menu = Menu(store_menu)

    start(best_buy, menu)


if __name__ == '__main__':
    main()
