from typing import List
from lunch_utils.base_models import IdModel
from lunch_utils.menu_models import (
    Menu,
    MenuHeader,
    MenuPositionValueObject,
    MenuValueObject,
)
from menu_repository import IMenuRepository


class IMenuController:
    """"
        Basic implementation of the menu controller.
        Only methods from repository are used.
    """
    def __init__(self, menu_repository: IMenuRepository):
        self.menu_repository = menu_repository

    def add_menu(self, menu: MenuHeader) -> IdModel:
        return self.menu_repository.save_menu(menu)

    def get_menu_by_id(self, menu_id: str) -> Menu:
        return self.menu_repository.get_menu_by_id(menu_id)

    def get_all_menu_headers(self) -> List[MenuHeader]:
        return self.menu_repository.get_all_menu_headers()

    def add_menu(self, menu: MenuValueObject) -> IdModel:
        return self.menu_repository.save_menu(menu)

    def update_menu(self, menu_id: str, menu: MenuValueObject) -> None:
        self.menu_repository.update_menu(menu_id, menu)

    def add_position(self, menu_id: str, position: Menu) -> IdModel:
        return self.menu_repository.add_position(menu_id, position)

    def remove_position(self, menu_id: str, position_id: str) -> None:
        self.menu_repository.remove_position(menu_id, position_id)

    def update_position(
        self, menu_id: str, position_id: str, new_position: MenuPositionValueObject
    ) -> None:
        self.menu_repository.update_position(menu_id, position_id, new_position)


class MenuController(IMenuController):
    """
        Temporary basic implementation of the menu controller from IMenuController is enough.
    """
    ...
