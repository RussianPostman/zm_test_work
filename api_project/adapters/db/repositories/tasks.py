from datetime import datetime

from sqlalchemy import update, select

from api_project.adapters.db.models import Task
from api_project.adapters.db.repositories import BaseRepository
from api_project.aplication.tasks.interfaces import TaskDatabaseInterface


class TaskRepository(BaseRepository, TaskDatabaseInterface):

    async def create_task(
        self,
        task_info: str,
        datetime_to_do: datetime,
    ) -> int:
        """
        Создаёт новую задачу.
        """
        async with self.get_session_maker()() as session:
            async with session.begin():
                new_task = Task(task_info=task_info, datetime_to_do=datetime_to_do)
                session.add(new_task)
                await session.flush()
                await session.refresh(new_task)
                return new_task.id


    async def get_task(
        self,
        task_id: int,
    ) -> dict | None:
        """
        Возвращает задачу по её ID.
        """
        async with self.get_session_maker()() as session:
            async with session.begin():
                query = await session.execute(
                    select(Task).where(Task.id == task_id)
                )

                if result := query.scalars().first():
                    return result.todict()

                return None


    async def get_tasks(
        self,
    ) -> list[dict[str, str | datetime]]:
        """
        Возвращает список задач.
        """
        async with self.get_session_maker()() as session:
            async with session.begin():
                result = await session.execute(select(Task))
                return [task.todict() for task in result.scalars().all()]


    async def update_task(
        self,
        task_id: int,
        task_info: str = None,
        datetime_to_do: datetime = None,
    ) -> dict[str, str | datetime] | None:
        """
        Обновляет задачу по её ID.
        """
        async with self.get_session_maker()() as session:
            async with session.begin():
                update_data = {}

                if task_info:
                    update_data["task_info"] = task_info
                if datetime_to_do:
                    update_data["datetime_to_do"] = datetime_to_do

                if update_data:
                    update_data['updated_at'] = datetime.now()
                    stmt = (
                        update(Task)
                        .where(Task.id == task_id)
                        .values(**update_data)
                        .returning(Task)
                    )
                    result = await session.execute(stmt)
                    updated_task = result.scalars().first()
                    await session.commit()

                    if updated_task:
                        return updated_task.todict()

                    return None

                return None
