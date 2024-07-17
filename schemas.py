from typing import Optional

from pydantic import BaseModel


class AddTask(BaseModel):
    name: str
    description: Optional[str] = None


class GetTask(AddTask):
    id: int


class GetTaskID(BaseModel):
    ok: bool = True
    task_id: int
