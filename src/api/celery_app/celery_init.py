from functools import cache

from celery import Celery
from celery.result import AsyncResult

from .celeryconfig import settings

# celery --broker redis://localhost:6379 --result-backend redis://localhost:6379 -A celery_app.celery worker --loglevel=INFO


@cache
def create_celery():
    celery = Celery("celery-worker")
    celery.config_from_object(settings, namespace="Celery")

    return celery


def get_task_info(task_id: str):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return result
