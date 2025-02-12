from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from . import BaseModel


class Task(BaseModel):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)
    datetime_to_do: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    task_info: Mapped[str]

    def todict(self) -> dict:
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'datetime_to_do': self.datetime_to_do,
            'task_info': self.task_info,
        }
