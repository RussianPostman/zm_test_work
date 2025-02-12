from api_project.adapters.db import Settings as DBSettings
from api_project.adapters.db.repositories.tasks import TaskRepository
from api_project.aplication.tasks.services import TaskService

db_settings = DBSettings()


task_repository = TaskRepository(db_settings.DATABASE_URL)

task_service = TaskService(task_repository)


def get_task_service() -> TaskService:
    return task_service
