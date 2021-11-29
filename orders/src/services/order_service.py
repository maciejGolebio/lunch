from abc import abstractmethod
from dependency_injector.wiring import inject

from lunch_utils.menu_models import Menu

import model
from lunch_utils.order_models import Order
from order_repository import IOrderRepository
from services.menu_service import IMenuService


class IOrderService:
    @abstractmethod
    def open_order(self, order: Order) -> None:

        raise NotImplementedError

@inject
class OrderService(IOrderService):
    def __init__(self, order_repository: IOrderRepository, menu_service: IMenuService):
        self.order_repository = order_repository
        self.menu_service = menu_service

    def open_order(self, order: Order, menu: Menu) -> None:
        order_model = model.OrderModel(order, menu)
        self.order_repository.create_order(order)

    # def close_order(self) -> None:
    #     self.order_model.close_order()
    #     self.order_repository.close_order(self.order_model.order.id)

    # def add_position(self, position: model.Position) -> None:
    #     self.order_model.add_position(position)
    #     self.order_repository.add_position(
    #         self.order_model.order.id,
    #         position.id,
    #         position.name,
    #         position.price,
    #         position.quantity,
    #     )

    # def remove_position(self, position_id: str) -> None:
    #     self.order_model.remove_position(position_id)
    #     self.order_repository.remove_position(
    #         self.order_model.order.id, position_id
    #     )

    # def update_position(self, position_id: str, position: model.Position) -> None:
    #     self.order_model.update_position(position_id, position)
    #     self.order_repository.update_position(
    #         self.order_model.order.id,
    #         position_id,
    #         position.name,
    #         position.price,
    #         position.quantity,
    #     )

    # def get_order_by_id(self, order_id: str) -> model.OrderView:
    #     order = self.order_repository.get_order_by_id(order_id)
    #     return model.OrderView(
    #         order.id,
    #         order.status,
    #         order.positions,
    #         order.created_at,
    #         order.updated_at,
    #     )

    # def update_order_status(self, order_id: str, order_status: str) -> None:
    #     self.order_repository.update_order_status(order_id, order_status)

    # def get_menu(self) -> model.MenuView:
    #     menu =
