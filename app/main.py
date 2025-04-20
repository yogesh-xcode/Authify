from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from app.routes.auth_routes import auth_router
from app.middlewares.jwt_middleware import jwt_middleware
from app.config.lifecycle import lifespan


app = FastAPI(lifespan=lifespan)
app.add_middleware(BaseHTTPMiddleware, dispatch=jwt_middleware)
app.include_router(router=auth_router)
