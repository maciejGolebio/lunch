from dependency_injector import containers, providers

from menu_repository import MenuRepository
from menu_controller import MenuController


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    menu_repository = providers.Factory(
        MenuRepository,
    )

    menu_controller = providers.Factory(
        MenuController,
        menu_repository=menu_repository,
    )
    