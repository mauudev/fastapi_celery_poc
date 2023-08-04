import os
from functools import cache

from kombu import Queue
from src.settings import APP_SETTINGS


def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "celery"}


class BaseConfig:
    broker_url = APP_SETTINGS.BROKER_URL
    result_backend = APP_SETTINGS.BACKEND_URL
    broker_connection_retry_on_startup = True
    task_default_queue = "celery-queue"
    imports = ["src.api.celery_app.tasks"]
    # CELERY_TASK_ROUTES = (route_task,)


class DevelopmentConfig(BaseConfig):
    ...


class ProductionConfig(BaseConfig):
    ...


@cache
def get_settings():
    config_cls_dict = {"development": DevelopmentConfig, "production": ProductionConfig}
    config_name = os.environ.get("CELERY_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
