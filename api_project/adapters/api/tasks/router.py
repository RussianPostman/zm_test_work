from fastapi import APIRouter, Body, Depends, HTTPException

from api_project.adapters.api.tasks.schemes import (
    CreateTaskReqest, CreateTaskResponse, Task, PatchTask
)
from api_project.aplication.app import get_task_service
from api_project.aplication.tasks.services import TaskService

task_router = APIRouter(
   prefix="/tasks",
   tags=["Задачи"],
)

@task_router.post("/create")
async def create_task(
    request: CreateTaskReqest = Body(),
    task_service: TaskService = Depends(get_task_service)
) -> CreateTaskResponse:
    return CreateTaskResponse.init(
        await task_service.create_task(
            task_info=request.task_info,
            datetime_to_do=request.datetime_to_do,
        )
    )

@task_router.get("/list")
async def list_tasks(
    task_service: TaskService = Depends(get_task_service),
):
    return [
        Task.init(task) for task in await task_service.get_tasks()
    ]

@task_router.get(
    "/{task_id}",
    response_model=Task
)
async def get_task(
    task_id: int,
    task_service: TaskService = Depends(get_task_service),
) -> Task:
    task_response = await task_service.get_task(
        task_id=task_id,
    )

    if task_response:
        return Task.init(task_response)

    else:
        raise HTTPException(
            status_code=400,
            detail='Несуществующий task_id',
        )


@task_router.patch(
    "/{task_id}/update",
    response_model=PatchTask
)
async def update_task(
    task_id: int,
    task_data: PatchTask,
    task_service: TaskService = Depends(get_task_service),
) -> Task:

    if not task_data.task_info and not task_data.datetime_to_do:
        raise HTTPException(
            status_code=400,
            detail='Нужно указать изменения'
        )

    task_response = await task_service.update_task(
        task_id=task_id,
        task_info=task_data.task_info,
        datetime_to_do=task_data.datetime_to_do,
    )

    if task_response:
        return Task.init(task_response)

    else:
        raise HTTPException(
            status_code=400,
            detail='Несуществующий task_id',
        )
