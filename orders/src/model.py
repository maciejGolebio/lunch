from typing import Dict
from uuid import UUID

from lunch_utils.menu_models import Menu
from lunch_utils.order_models import Order, OrderStatus


class OrderModel:
    def __init__(self, order: Order, menu: Menu):
        self.order = order
        self.menu = menu

    def close_order(self):
        self.order.status = OrderStatus.CLOSED

    def add_position(self, position):
        self.order.positions.append(position)

    def remove_position(self, position_id: str):
        self.order.positions = [
            elem for elem in self.order.positions if elem.id != position_id
        ]

    def update_position(self, position_id: str, position):
        self.order.positions = [
            elem if elem.id != position_id else position
            for elem in self.order.positions
        ]

    @property
    def total_price(self):
        return sum(elem.price for elem in self.order.positions)

    @property
    def order_report(self):
        positions = self.__count_positions()
        return {k: self.__extend_report_position(k, v) for k, v in positions.items()}

    @property
    def list_of_purchasers(self):
        ...

    def __count_positions(self) -> Dict[UUID, int]:
        postitions = {}
        for elem in self.order.positions:
            postitions[elem.id] = (
                1 if elem.id not in postitions else postitions[elem.id] + 1
            )
        return postitions

    def __extend_report_position(self, postion_id: UUID, count: int):
        position = next(
            elem for elem in self.order.positions if elem.postion_id == postion_id
        )
        # TODO: replace by dataclass
        return {"count": count, "postion": position}

