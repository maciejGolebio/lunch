from typing import List
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from lunch_utils.base_models import IdModel
from lunch_utils.menu_models import Menu, MenuHeader, MenuPositionValueObject
from menu_boostrap import Container
from menu_controller import IMenuController

router = APIRouter()
from uuid import UUID

@router.post("/menu", response_model=IdModel)
@inject
def create_menu(
    menu: MenuHeader,
    menu_controller: IMenuController = Depends(Provide[Container.menu_controller]),
):
    return menu_controller.add_menu(menu)


@router.get("/menu", response_model=List[MenuHeader])
@inject
def get_all_menu_headers(
    menu_controller: IMenuController = Depends(Provide[Container.menu_controller]),
):
    return menu_controller.get_all_menu_headers()


@router.get("/menu/{menu_id}", response_model=Menu)
@inject
def get_menu_by_id(
    menu_id: UUID,
    menu_controller: IMenuController = Depends(Provide[Container.menu_controller]),
):
    return menu_controller.get_menu_by_id(menu_id)


@router.post("/menu/{menu_id}/position", response_model=IdModel)
@inject
def add_position(
    menu_id: str,
    position: MenuPositionValueObject,
    menu_controller: IMenuController = Depends(Provide[Container.menu_controller]),
):
    return menu_controller.add_position(menu_id, position)


@router.delete("/menu/{menu_id}/position/{position_id}")
@inject
def remove_position(
    menu_id: str,
    position_id: str,
    menu_controller: IMenuController = Depends(Provide[Container.menu_controller]),
):
    menu_controller.remove_position(menu_id, position_id)


@router.put("/menu/{menu_id}/position/{position_id}")
@inject
def update_position(
    menu_id: str,
    position_id: str,
    new_position: MenuPositionValueObject,
    menu_controller: IMenuController = Depends(Provide[Container.menu_controller]),
):
    menu_controller.update_position(menu_id, position_id, new_position)
