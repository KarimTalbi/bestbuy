from dataclasses import dataclass


@dataclass()
class MenuObject:
    menu_items: list[str]
    header: str | None = None
    seperator: str | None = None
    footer: str | None = None


class Menu:

    def __init__(self, menu_obj: MenuObject):
        self._menu = menu_obj
        self._top_sep = True
        self._bot_sep = False

    @property
    def header(self) -> str:
        return self._menu.header

    @property
    def seperator(self) -> str:
        return self._menu.seperator

    @property
    def footer(self) -> str:
        return self._menu.footer

    @property
    def menu_items(self) -> list[str]:
        return self._menu.menu_items

    def add_menu_item(self, menu_item: str) -> None:
        self._menu.menu_items.append(menu_item)

    def del_menu_item(self, menu_item: str) -> None:
        self._menu.menu_items.remove(menu_item)

    def set_header(self, header: str) -> None:
        self._menu.header = header

    def set_seperator(self, seperator: str) -> None:
        self._menu.seperator = seperator

    def set_top_sep(self, enable: bool) -> None:
        self._top_sep = enable

    def set_bot_sep(self, enable: bool) -> None:
        self._bot_sep = enable

    @property
    def _create_options(self):
        options = []
        for i in range(len(self._menu.menu_items)):
            options.append(f'{i + 1}. {self._menu.menu_items[i]}')
        return "\n".join(options)

    @property
    def show_menu(self):
        output = "\n"
        if self.header:
            output += f"{self.header}\n"
        if self._top_sep:
            output += f"{self.seperator}\n"
        output += self._create_options
        if self._bot_sep:
            output += f"{self.seperator}\n"
        if self.footer:
            output += f"{self.footer}\n"
        return output

    def __str__(self):
        return self.show_menu
