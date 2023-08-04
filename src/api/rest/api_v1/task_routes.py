from fastapi import APIRouter
from src import logger
from src.api.celery_app.celery_init import get_task_info
from src.api.celery_app.tasks import add, div, long_running_task, mul

from . import schemas as api_model

router = APIRouter(prefix="/tasks")


@router.get(
    "/long-running",
    operation_id="long_running_tasks",
)
async def long_running_tasks() -> api_model.TaskSent:
    task_id = long_running_task.apply_async(args=[2])
    logger.info(f"Task sent successfully: {task_id}")
    return api_model.TaskSent(task_id=str(task_id))


@router.post(
    "/add",
    response_model=api_model.TaskSent,
    operation_id="add_task",
)
async def add_task(
    task_req: api_model.AddTask,
) -> api_model.TaskSent:
    task_id = add.apply_async(args=[task_req.x, task_req.y])
    logger.info(f"Task sent successfully: {task_id}")
    return api_model.TaskSent(task_id=str(task_id))


@router.post(
    "/mul",
    response_model=api_model.TaskSent,
    operation_id="mul_task",
)
async def mul_task(
    task_req: api_model.MulTask,
) -> api_model.TaskSent:
    task_id = mul.apply_async(args=[task_req.x, task_req.y])
    logger.info(f"Task sent successfully: {task_id}")
    return api_model.TaskSent(task_id=str(task_id))


@router.post(
    "/div",
    response_model=api_model.TaskSent,
    operation_id="div_task",
)
async def div_task(
    task_req: api_model.DivTask,
) -> api_model.TaskSent:
    task_id = div.apply_async(args=[task_req.x, task_req.y])
    logger.info(f"Task sent successfully: {task_id}")
    return api_model.TaskSent(task_id=str(task_id))


@router.get(
    "/result/{task_id}",
    response_model=api_model.TaskRes,
    operation_id="task_result",
)
async def task_result(task_id: str) -> api_model.TaskRes:
    task_info = get_task_info(task_id)
    return api_model.TaskRes(**task_info)
