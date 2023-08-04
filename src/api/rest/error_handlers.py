from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ApiRestError(BaseModel):
    detail: str


def unknown_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ApiRestError(detail=str(exc)).dict(),
    )


def add_error_handler(app: FastAPI) -> FastAPI:
    app.add_exception_handler(Exception, unknown_exception)
    return app
