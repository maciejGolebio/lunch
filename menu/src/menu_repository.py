import json
import uuid
from abc import ABC, abstractmethod
from os import listdir
from typing import List

from lunch_utils.base_models import IdModel
from lunch_utils.base_repository import BaseRepository
from lunch_utils.menu_models import (
    EmptyMenu,
    Menu,
    MenuHeader,
    MenuPosition,
    MenuPositionValueObject,
    MenuValueObject,
)
from pydantic import BaseModel


class IMenuRepository(ABC, BaseRepository):
    @abstractmethod
    def get_menu_by_id(self, menu_id: str) -> Menu:
        ...

    @abstractmethod
    def get_all_menu_headers(self) -> List[MenuHeader]:
        ...

    @abstractmethod
    def save_menu(self, menu: MenuHeader) -> IdModel:
        ...

    @abstractmethod
    def update_menu(self, menu_id: str, menu: MenuValueObject) -> None:
        ...

    @abstractmethod
    def add_position(self, menu_id: str, position: MenuPositionValueObject) -> IdModel:
        ...

    @abstractmethod
    def remove_position(self, menu_id: str, position_id: str) -> None:
        ...

    @abstractmethod
    def update_position(
        self, menu_id: str, position_id: str, new_position: MenuPositionValueObject
    ) -> None:
        ...


class MenuRepository(IMenuRepository):
    def __init__(self, database=None) -> None:
        self.database = database

    def get_menu_by_id(self, menu_id: str) -> Menu:
        self.__read_menu_from_id(menu_id)

    def get_all_menu_headers(self) -> List[MenuHeader]:
        list_headers = []
        for menu_file in listdir("./db"):
            list_headers.append(self.__read_menu_from_file(menu_file, MenuHeader))
        print(list_headers)
        return list_headers

    def save_menu(self, menu: MenuHeader) -> IdModel:
        menu_id = str(uuid.uuid4())
        full_model = self.__convert_menu_value_to_empty_menu(menu_id, menu)
        self.__write_menu(full_model)
        return IdModel(id=menu_id)

    def update_menu(self, menu_id: str, menu: MenuValueObject) -> None:
        full_model = self.__convert_menu_value_to_menu(menu, menu_id)
        self.__write_menu(full_model)

    def add_position(self, menu_id: str, position: MenuPositionValueObject) -> IdModel:
        menu: Menu = self.__read_menu_from_id(menu_id)
        position_id = str(uuid.uuid4())
        full_model = self.__convert_postion_value_to_postion(position, position_id)
        menu.positions.append(full_model)
        self.__write_menu(menu)
        return IdModel(id=position_id)

    def remove_position(self, menu_id: str, position_id: str) -> None:
        menu: Menu = self.__read_menu_from_id(menu_id)
        menu.positions = [
            position for position in menu.positions if position.id != position_id
        ]
        self.__write_menu(menu)

    def update_position(
        self, menu_id: str, position_id: str, new_position: MenuPositionValueObject
    ) -> None:
        menu: Menu = self.__read_menu_from_id(menu_id)
        full_model = self.__convert_postion_value_to_postion(new_position, position_id)
        menu.positions = [
            full_model if position.id == position_id else position
            for position in menu.positions
        ]
        self.__write_menu(menu)

    @staticmethod
    def __read_menu_from_file(
        menu_file: str, menu_model: BaseModel = Menu
    ) -> BaseModel:
        with open(f"db/{menu_file}", "r") as menu_file:
            return menu_model.parse_obj(json.load(menu_file))

    @staticmethod
    def __read_menu_from_id(menu_id: str, menu_model: BaseModel = Menu) -> BaseModel:
        with open(f"db/{menu_id}.json", "r") as menu_file:
            return menu_model.parse_obj(json.load(menu_file))

    @staticmethod
    def __write_menu(menu: Menu) -> None:
        with open(f"db/{menu.id}.json", "w") as menu_file:
            menu_file.write(menu.json())

    @staticmethod
    def __convert_menu_value_to_menu(menu_value: MenuValueObject, menu_id: str) -> Menu:
        return Menu(id=menu_id, **menu_value.dict())

    @staticmethod
    def __convert_menu_value_to_empty_menu(
        menu_id, menu_value: MenuHeader
    ) -> EmptyMenu:
        return EmptyMenu(id=menu_id, **menu_value.dict())

    @staticmethod
    def __convert_postion_value_to_postion(
        postion_value: MenuPositionValueObject, position_id: str
    ) -> MenuPosition:
        return MenuPosition(id=position_id, **postion_value.dict())
