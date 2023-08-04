from fastapi import FastAPI
from src.api.rest.api_v1 import task_routes


def build_routes(app: FastAPI) -> FastAPI:
    app.include_router(task_routes.router, prefix="/v1")

    return app
