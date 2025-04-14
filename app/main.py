from fastapi import FastAPI
from app.routes.auth_routes import auth_router
from app.config.lifecycle import lifespan


app = FastAPI(lifespan=lifespan)

app.include_router(router=auth_router)
