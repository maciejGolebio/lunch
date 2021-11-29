from typing import List, Optional
from pydantic import BaseModel

from lunch_utils.base_models import IdModel


class MenuPositionValueObject(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    is_spicy: Optional[bool] = None
    is_veg: Optional[bool] = None


class MenuPosition(IdModel, MenuPositionValueObject):
    ...


class MenuHeader(BaseModel):
    restaurnat_name: str
    menu_name: Optional[str] = None
    description: Optional[str] = None


class MenuValueObject(MenuHeader):
    positions: Optional[List[MenuPosition]]


class EmptyMenu(IdModel, MenuHeader):
    ...


class Menu(IdModel, MenuValueObject):
    ...
