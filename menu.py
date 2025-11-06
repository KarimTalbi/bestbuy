"""
This module provides functionality for creating and managing a textual menu
representation using the `MenuObject` dataclass and the `Menu` class.

The `MenuObject` dataclass acts as a structure for storing menu-related data,
while the `Menu` class supplies methods for building, displaying, and modifying
the menu, including operations like adding or removing menu items and setting
menu headers, separators, and footers. The `Menu` class also provides a stringified
representation of the menu state.
"""
from dataclasses import dataclass


@dataclass()
class MenuObject:
    """
    Represents a menu structure with items, header, separator, and footer.

    This class is used to organize and structure menus, providing additional
    properties such as a header, separator, and footer to customize the menu
    display.

    :ivar menu_items: A list of strings representing menu items.
    :ivar header: An optional string for the menu header.
    :ivar seperator: An optional string for the menu separator.
    :ivar footer: An optional string for the menu footer.
    """
    menu_items: list[str]
    header: str | None = None
    seperator: str | None = None
    footer: str | None = None


class Menu:
    """
    Represents a menu system with customizable header, footer, separators, and menu items.

    This class provides a flexible way to manage and render a menu. The menu can have a
    custom header, footer, and separators, and allows dynamic addition and removal of
    menu items. It also supports enabling or disabling top and bottom separators. The menu
    is rendered as a formatted string when requested.

    :ivar header: The header text of the menu.
    :type header: str
    :ivar seperator: The string used as a separator in the menu.
    :type seperator: str
    :ivar footer: The footer text of the menu.
    :type footer: str
    :ivar menu_items: A list of strings representing the menu items.
    :type menu_items: list[str]
    """

    def __init__(self, menu_obj: MenuObject):
        """
        Initializes an object with a menu instance and separator flags.

        :param menu_obj: The menu object used to initialize the class.
        :type menu_obj: MenuObject
        """
        self._menu = menu_obj
        self._top_sep = True
        self._bot_sep = False

    @property
    def header(self) -> str:
        """
        Retrieves the header attribute from the internal _menu object.

        :returns: The header string of the menu object.
        :rtype: str
        """
        return self._menu.header

    @property
    def seperator(self) -> str:
        """
        Retrieves the seperator attribute from the internal _menu object.

        :return: The separator string which determines the menu item formatting.
        :rtype: str
        """
        return self._menu.seperator

    @property
    def footer(self) -> str:
        """
        Retrieves the footer attribute from the internal _menu object.

        :return: The footer text.
        :rtype: str
        """
        return self._menu.footer

    @property
    def menu_items(self) -> list[str]:
        """
        Retrieves the list of menu items.

        :return: A list of strings representing menu items.
        :rtype: list[str]
        """
        return self._menu.menu_items

    def add_menu_item(self, menu_item: str) -> None:
        """
        Adds a new menu item to the menu.

        :param menu_item: The name of the menu item to be added.
        :type menu_item: str
        """
        self._menu.menu_items.append(menu_item)

    def del_menu_item(self, menu_item: str) -> None:
        """
        Removes a menu item from the menu.

        :param menu_item: The name of the menu item to be removed.
        :type menu_item: str
        """
        self._menu.menu_items.remove(menu_item)

    def set_header(self, header: str) -> None:
        """
        Sets the header for the menu.

        :param header: The new header string to set for the menu.
        :type header: str
        """
        self._menu.header = header

    def set_seperator(self, seperator: str) -> None:
        """
        Sets the menu separator to a given string.

        :param seperator: The string value to define the new menu
            separator.
        :type seperator: str
        """
        self._menu.seperator = seperator

    def set_top_sep(self, enable: bool) -> None:
        """
        Sets the state of the top separator.

        :param enable: Determines whether the top separator should be enabled or
            disabled.
        :type enable: bool
        """
        self._top_sep = enable

    def set_bot_sep(self, enable: bool) -> None:
        """
        Sets the bot separation behavior within the system.

        :param enable: A boolean indicating whether to enable or disable the bot
                separation.
        """
        self._bot_sep = enable

    @property
    def _create_options(self):
        """
        Constructs and returns formatted menu options as a string.

        :return: A string containing formatted menu options, where each option is
            represented as a numbered item from the menu.
        :rtype: str
        """
        options = []
        for i in range(len(self._menu.menu_items)):
            options.append(f'{i + 1}. {self._menu.menu_items[i]}')
        return "\n".join(options)

    @property
    def show_menu(self):
        """
        Provides the formatted menu string for display, including optional header,
        footer, separators, and menu options.

        :return: A string representing the formatted menu content.
        :rtype: str
        """
        output = "\n"

        if self.header:
            output += f"{self.header}\n"

        if self._top_sep:
            output += f"{self.seperator}\n"

        output += f"{self._create_options}\n"

        if self._bot_sep:
            output += f"{self.seperator}\n"

        if self.footer:
            output += f"{self.footer}"

        return output

    def __str__(self):
        """
        Converts the object to its string representation.

        This method is called when `str()` or `print()` is invoked on the object.

        :return: String representation of the object.
        :rtype: str
        """
        return self.show_menu
