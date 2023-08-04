import time

from celery import Task, shared_task
from src import logger


class LongRunningTask(Task):
    def __init__(self):
        super().__init__()
        self.status = None

    def run(self, *args, **kwargs):
        logger.info("Executing long running tasks ..")
        try:
            self.execute(*args, **kwargs)
        finally:
            self.status = "FINISHED"

    def execute(self, sleep: int):
        if not self.status:
            self.status = "RUNNING"
        self.heavy_task(sleep)
        self.lightweight_task(sleep)
        self.soft_task(sleep)

    def heavy_task(self, sleep: int):
        time.sleep(sleep + 10)
        logger.info("Heavy task completed ..")

    def lightweight_task(self, sleep: int):
        time.sleep(sleep + 5)
        logger.info("Lightweight task completed ..")

    def soft_task(self, sleep: int):
        time.sleep(sleep + 3)
        logger.info("Soft task completed ..")


@shared_task(bind=True, base=LongRunningTask)
def long_running_task(self, sleep: int):
    self.execute(sleep)


@shared_task
def add(x: int, y: int):
    result = x + y
    return result


@shared_task
def mul(x: int, y: int):
    result = x * y
    return result


@shared_task
def div(x: int, y: int):
    result = x / y
    return result
