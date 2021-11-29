from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from lunch_utils.base_models import IdModel

import order_boot
from services import id_service, menu_service, order_service

router = APIRouter()


@router.post("/order", response_model=IdModel)
@inject
def create_order(
    menu_service: menu_service.IMenuService = Depends(
        Provide[order_boot.Container.menu_service]
    ),
    order_service: order_service.IOrderService = Depends(
        Provide[order_boot.Container.order_service]
    ),
    id_service: id_service.IIDService = Depends(
        Provide[order_boot.Container.id_service]
    ),
):
    order_id = id_service.get_id()
    # Validate menu_id
    # Open order
    return IdModel(id=order_id)
