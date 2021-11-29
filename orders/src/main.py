from fastapi import FastAPI
from order_boot import Container
import order_router


def initialize():
    container = Container()
    container.wire(modules=[order_router])
    app = FastAPI()
    app.container = container
    app.include_router(order_router.router)
    return app


app = initialize()
