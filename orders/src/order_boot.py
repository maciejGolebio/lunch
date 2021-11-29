from dependency_injector import containers, providers

from order_repository import OrderRepository
from services.order_service import OrderService
from services.menu_service import MenuService
from services.id_service import IDService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    order_repository = providers.Factory(OrderRepository)

    id_service = providers.Factory(IDService)

    menu_service = providers.Factory(MenuService, menu_url=config.services.menu_url)

    order_service = providers.Factory(
        OrderService, order_repository=order_repository, menu_service=menu_service
    )
