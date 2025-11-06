"""
Defines custom exceptions and the Product class for managing product inventory and actions.

This module includes custom exception classes for handling specific error conditions and the
Product class, which represents an item in inventory with attributes like name, price, quantity,
and active status. The Product class provides methods to activate/deactivate a product, manage
quantities, and calculate the cost of purchases.
"""


class EmptyParamError(Exception):
    """
    Exception raised when a required parameter is missing.
    """
    pass


class TypeParamError(Exception):
    """
    Exception raised for errors related to incorrect type parameter usage.
    """
    pass


class NegativeParamError(Exception):
    """
    Exception raised when a negative parameter is provided.
    """
    pass


class OutOfStockError(Exception):
    """
    Custom exception raised when an item is out of stock.
    """
    pass


class Product:
    """
    Represents a product with attributes for its name, price, quantity, and activation status.

    The Product class is responsible for managing inventory and allowing interactions such as
    activating, deactivating, purchasing products, and displaying their details.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a new instance of the class with the provided name, price, and quantity. Ensures
        that the attributes are properly validated before being assigned to the instance.

        :param name: Name of the product
        :type name: str
        :param price: Price of the product
        :type price: float
        :param quantity: Quantity of the product in stock
        :type quantity: int
        """
        self._init_check(name, price, quantity)
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

    @staticmethod
    def _init_check(name: str, price: float, quantity: int):
        """
        Performs validation checks on provided parameters to ensure they adhere to the expected
        constraints and types. Raises appropriate exceptions if any of the conditions are not met.

        :param name: The name of the item being validated
        :param price: The price value of the item being validated. Must be a non-negative float or int
        :param quantity: The quantity value of the item being validated. Must be a non-negative integer
        :raises EmptyParamError: If any of the arguments is None or empty
        :raises TypeParamError: If the type of argument does not match the expected type
        :raises NegativeParamError: If price or quantity is less than zero
        """
        if not name or not price or not quantity:
            raise EmptyParamError("Arguments can't be empty / of type None")

        if not isinstance(name, str) or not isinstance(price, float | int) or not isinstance(quantity, int):
            raise TypeParamError("Check the type of the arguments - name: str, price: float, quantity: int")

        if price < 0 or quantity < 0:
            raise NegativeParamError("price and quantity values must be positive")

    def get_quantity(self) -> int:
        """
        Retrieves the quantity value.

        :return: The quantity as an integer
        :rtype: int
        """
        return self._quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity value for the object. If the provided quantity is less
        than or equal to zero, the object will be deactivated.

        :param quantity: A positive integer representing the new quantity to be set.
        """
        self._quantity = quantity
        if self._quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Checks whether the object is in an active state.

        :return: Boolean value indicating if the object is active.
        :rtype: bool
        """
        return self._active

    def activate(self):
        """
        Activates the object functionality by setting its state to active.
        """
        self._active = True

    def deactivate(self):
        """
        Deactivates the current object by setting its active state to False.
        """
        self._active = False

    def show(self):
        """
        Displays the name, price, and quantity of the item.
        """
        print(f"{self._name}, Price: {self._price}, Quantity: {self._quantity}")

    def buy(self, quantity: int) -> float:
        """
        Calculates the total cost of buying a specified quantity of an item and reduces
        the item's stock accordingly. If the requested quantity exceeds the current stock,
        an error is raised. Returns the total cost for the specified quantity.

        :param quantity: The number of items to buy.
        :type quantity: int
        :return: The total cost for the specified quantity.
        :rtype: float
        :raises OutOfStockError: If the requested quantity exceeds the available stock.
        """
        stock = self.get_quantity()
        left = stock - quantity
        if left < 0:
            raise OutOfStockError(f"Not enough items of '{self._name}' in stock. Current stock: {stock}")
        self.set_quantity(left)
        return quantity * self._price
