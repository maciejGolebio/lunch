from abc import abstractmethod
from typing import List

from lunch_utils.base_repository import BaseRepository
from lunch_utils.order_models import Order, OrderHeader, OrderView


class IOrderRepository(BaseRepository):
    @abstractmethod
    def get_all_orders(self) -> List[OrderHeader]:
        ...

    @abstractmethod
    def get_order_by_id(self, order_id: str) -> OrderView:
        ...

    @abstractmethod
    def updade_order_status(self, order_id: str, order_status: str) -> None:
        ...

    @abstractmethod
    def create_order(self, order: Order) -> None:
        ...

    @abstractmethod
    def close_order(self, order_id: str) -> None:
        ...


class OrderRepository(IOrderRepository):
    def __init__(self):
        self.orders = []

    def create_order(self, order: Order) -> None:
        self.orders.append(order)
    