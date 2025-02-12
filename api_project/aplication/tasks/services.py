from dataclasses import dataclass
from datetime import datetime

from api_project.aplication.tasks.interfaces import TaskDatabaseInterface


@dataclass
class TaskService:
    """
    Т.к в этом приложении бизнес логики нет, слой приложения в целом избыточен.
    Однако, он тут есть не только потому, что мне лень его вырезать, но и за тем,
    чтобы не дёргать базу данных из слоя представления.
    """
    database: TaskDatabaseInterface

    async def create_task(
        self,
        task_info: str,
        datetime_to_do: datetime
    ) -> int:
        return await self.database.create_task(
            task_info=task_info,
            datetime_to_do=datetime_to_do,
        )

    async def get_task(
        self,
        task_id: int,
    ):
        return await self.database.get_task(task_id=task_id)

    async def get_tasks(
        self,
    ):
        return await self.database.get_tasks()

    async def update_task(
            self,
            task_id: int,
            task_info: str = None,
            datetime_to_do: datetime = None,
    ) -> dict[str, str | datetime] | None:
        return await self.database.update_task(
            task_id=task_id,
            task_info=task_info,
            datetime_to_do=datetime_to_do,
        )
