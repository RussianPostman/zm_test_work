from abc import ABC, abstractmethod
from datetime import datetime


class TaskDatabaseInterface(ABC):

    @abstractmethod
    async def create_task(
        self,
        task_info: str,
        datetime_to_do: datetime
    ):
        """
        Создаёт новую задачу
        """
        ...

    @abstractmethod
    async def get_task(
        self,
        task_id: int,
    ):
        """
        Возвращает задачу по её ID.
        """
        ...

    @abstractmethod
    async def get_tasks(
        self,
    ):
        """
        Возвращает список задач.
        """
        ...

    @abstractmethod
    async def update_task(
        self,
        task_id: int,
        task_info: str = None,
        datetime_to_do: datetime = None,
    ):
        """
        Обновляет задачу по её ID.
        """
        ...
