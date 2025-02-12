from datetime import datetime

from pydantic import BaseModel


class CreateTaskReqest(BaseModel):
    task_info: str
    datetime_to_do: datetime


class CreateTaskResponse(BaseModel):
    task_id: int

    @classmethod
    def init(cls, task_id: int):
        return cls(task_id=task_id)


class GetTaskReqest(BaseModel):
    task_id: int


class Task(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    datetime_to_do: datetime
    task_info: str

    @classmethod
    def init(cls, task: dict):
        return cls(
            id=task.get('id'),
            created_at=task.get('created_at'),
            updated_at=task.get('updated_at'),
            datetime_to_do=task.get('datetime_to_do'),
            task_info=task.get('task_info'),
        )


class PatchTask(BaseModel):
    datetime_to_do: datetime | None = None
    task_info: str | None = None

