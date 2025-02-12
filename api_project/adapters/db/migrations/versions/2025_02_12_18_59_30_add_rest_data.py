"""add rest data

Revision ID: 738e2fb18782
Revises: 0008da1bb94e
Create Date: 2025-02-12 18:59:30.265279

"""
from dataclasses import dataclass
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '738e2fb18782'
down_revision: Union[str, None] = '0008da1bb94e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


@dataclass
class Task:
    datetime_to_do: datetime
    task_info: str


task_table = sa.table(
    'tasks',
    sa.column('id', sa.Integer),
    sa.column('task_info', sa.Unicode),
    sa.column('datetime_to_do', sa.DateTime),
)


base_tasks = [
    Task(task_info='Первая дефолтная задача', datetime_to_do=datetime(2030, 1, 1)),
    Task(task_info='Вторая дефолтная задача', datetime_to_do=datetime(2030, 1, 1)),
    Task(task_info='Третья дефолтная задача', datetime_to_do=datetime(2030, 1, 1)),
    Task(task_info='Четвёртая дефолтная задача', datetime_to_do=datetime(2030, 1, 1)),
]


def upgrade() -> None:
    # connection = op.get_bind()

    for task in base_tasks:
        op.execute(task_table.insert().values(task.__dict__))


def downgrade() -> None:
    connection = op.get_bind()

    for task in base_tasks:
        connection.execute(
            task_table
            .delete()
            .where(
                task_table.c.task_info == task.task_info,
                task_table.c.datetime_to_do == task.datetime_to_do,
            )
        )
