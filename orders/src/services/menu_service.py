from abc import abstractmethod

from uuid import UUID

from lunch_utils.menu_models import Menu
import requests
from pydantic import HttpUrl


class IMenuService:
    @abstractmethod
    def get_menu_by_id(self, menu_id: UUID) -> Menu:
        ...

    @staticmethod
    @abstractmethod
    def validate_position(position_id: UUID, menu: Menu) -> bool:
        ...


class MenuService(IMenuService):
    def __init__(self, menu_url: HttpUrl):
        self.menu_url = menu_url

    def get_menu_by_id(self, menu_id: UUID) -> Menu:
        resp = requests.get(f"{self.menu_url}/{menu_id}")
        if resp.status_code != 200:
            raise MenuNotExists
        return Menu.parse_obj(resp.json())

    @staticmethod
    def validate_position(position_id: UUID, menu: Menu) -> bool:
        return bool([elem for elem in menu.positions if elem.id == position_id])


class MenuNotExists(Exception):
    ...
