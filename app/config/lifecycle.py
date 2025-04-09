from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import db_init

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_init()
    yield