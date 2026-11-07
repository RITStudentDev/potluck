from fastapi import FastAPI
from contextlib import asynccontextmanager
from .models import Base
from .database import engine
from .api import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router)