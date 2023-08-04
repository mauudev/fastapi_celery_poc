import uvicorn
from fastapi import FastAPI
from src import logger
from src.api.celery_app.celery_init import create_celery
from src.api.rest.error_handlers import add_error_handler
from src.api.rest.route_builder import build_routes
from src.settings import APP_SETTINGS

app = FastAPI()
app = add_error_handler(app)
app = build_routes(app)
app.celery_app = create_celery()
celery = app.celery_app


@app.get("/")
async def root():
    return {"message": "Hello from main server !"}


def start_server():
    logger.info(
        f"Started server running on host: http://{APP_SETTINGS.API_HOST}:{APP_SETTINGS.API_PORT}"
    )
    uvicorn.run(
        "src.api.main:app",
        host=APP_SETTINGS.API_HOST,
        port=int(APP_SETTINGS.API_PORT),
        log_level="info",
        reload=True,
    )


if __name__ == "__main__":
    start_server()
