from pydantic import BaseModel


class AddTask(BaseModel):
    x: int
    y: int


class MulTask(BaseModel):
    x: int
    y: int


class DivTask(BaseModel):
    x: int
    y: int


class TaskRes(BaseModel):
    task_id: str
    task_status: str
    task_result: int | float


class TaskSent(BaseModel):
    task_id: str
