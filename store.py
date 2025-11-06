"""
This module provides functionality for managing a store's product inventory.

It includes the `Store` class, which allows adding, removing, and retrieving
products, computing the total quantity of items in stock, and processing
customer orders. The module encapsulates store inventory management operations.
"""
from products import Product


class Store:
    """
    A store class that manages a collection of products.

    The Store class provides methods to add, remove, and retrieve products, compute the total
    quantity of items, and process customer orders. It serves as a representation of an inventory
    system where the products are stored and managed effectively.
    """

    def __init__(self, products: list[Product]):
        """
        Initializes an instance with a list of products.

        :param products: A list of `Product` instances representing the products
            to be included in the stock.
        :type products: list[Product]
        """
        self._stock = products

    def add_product(self, product: Product):
        """
        Adds a product to the stock.

        :param product: The product to be added to the stock
        :type product: Product
        """
        self._stock.append(product)

    def remove_product(self, product: Product):
        """
        Removes a specified product from the stock.

        :param product: The product instance to be removed from the stock.
        :type product: Product
        """
        self._stock.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates and returns the total quantity of items in stock.

        :return: Total quantity of items in the stock.
        :rtype: int
        """
        return sum([item.get_quantity() for item in self._stock])

    def get_all_products(self) -> list[Product]:
        """
        Retrieves all active products from the stock.

        :return: A list of active `Product` objects from the stock.
        :rtype: list[Product]
        """
        return [item for item in self._stock if item.is_active()]

    def show_all(self) -> str:
        """
        Generates a formatted string displaying a list of all available products.

        :return: A formatted string representing the list of all available products.
        :rtype: str
        """
        output = "------\n"
        for i, item in enumerate(self.get_all_products()):
            output += f"{i + 1}. {item._name}, Price: {item._price}, Quantity: {item._quantity}\n"
        return output + "------"

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Calculates the total cost of purchasing items from the shopping list.

        :param shopping_list: A list of tuples, where each tuple contains a `Product` and an
            integer representing the quantity to be purchased.
        :type shopping_list: list[tuple[Product, int]]
        :return: The total cost of purchasing all items from the shopping list.
        :rtype: float
        """
        total = 0
        for item in shopping_list:
            total += item[0].buy(item[1])
        return total
