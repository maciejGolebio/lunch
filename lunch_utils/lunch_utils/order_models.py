from typing import List
from pydantic import BaseModel
from lunch_utils.base_models import IdModel
from enum import Enum

from uuid import UUID


class OrderStatus(str, Enum):
    OPEN = "open"
    CLOSED = "closed"


class OrderPositionCreate(BaseModel):
    position_id: UUID
    menu_id: UUID
    price: float
    user_email: str


class OrderPosition(IdModel, OrderPositionCreate):
    ...


class OrderPositionView(OrderPosition):
    price: float


class OrderHeader(BaseModel):
    payment_method_details: str
    user_email: str
    menu_id: str
    status: OrderStatus


class Order(IdModel, OrderHeader):
    positions: List[OrderPosition]


class OrderView(OrderHeader):
    positions: List[OrderPositionView]
