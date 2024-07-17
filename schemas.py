from typing import Optional

from pydantic import BaseModel, ConfigDict


class AddTask(BaseModel):
    name: str
    description: Optional[str] = None


class GetTask(AddTask):
    id: int

    model_config = ConfigDict(from_attributes=True)


class GetTaskID(BaseModel):
    ok: bool = True
    task_id: int
