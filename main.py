from typing import Annotated

from fastapi import FastAPI, Depends

from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import AddTask
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Clear')
    await create_tables()
    print('Ready')
    yield
    print('Off')


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)



