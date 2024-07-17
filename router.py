from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import AddTask, GetTaskID

router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.post('')
async def add_task(task: Annotated[AddTask, Depends()]) -> GetTaskID:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get('')
async def get_task() -> list[AddTask]:
    tasks = await TaskRepository.get_all()
    return tasks
