from fastapi import FastAPI
from app.routes.auth_routes import auth_router
from app.config.database import db_init
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_init()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=auth_router)
