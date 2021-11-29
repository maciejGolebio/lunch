from fastapi import FastAPI
from menu_boostrap import Container
import menu_router


def initialize():
    container = Container()
    container.wire(modules=[menu_router])
    app = FastAPI()
    app.container = container
    app.include_router(menu_router.router)
    return app


app = initialize()
