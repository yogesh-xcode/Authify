from fastapi import FastAPI
from app.routes.AuthRoutes import auth_router

app = FastAPI()

app.include_router(router=auth_router, tags=["Authendication routes"])


@app.get("/")
def welcome():
    return {"message": "Welcome to Authify for docs go /docs"}
