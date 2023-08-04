from functools import cache

from celery import Celery
from celery.result import AsyncResult

from .celeryconfig import settings

# celery --broker redis://localhost:6379 --result-backend redis://localhost:6379 -A celery_app.celery worker --loglevel=INFO


@cache
def create_celery():
    celery = Celery("celery-worker")
    celery.config_from_object(settings, namespace="Celery")
    celery.conf.update(task_track_started=True)
    celery.conf.update(task_serializer="pickle")
    celery.conf.update(result_serializer="pickle")
    celery.conf.update(accept_content=["pickle", "json"])
    celery.conf.update(result_persistent=True)
    celery.conf.update(worker_send_task_events=False)
    celery.conf.update(worker_prefetch_multiplier=1)

    return celery


def get_task_info(task_id: str):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return result
