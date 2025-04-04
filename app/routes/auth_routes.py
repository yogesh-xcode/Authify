from fastapi import APIRouter
from app.models.AuthModel import RegisterModel, LoginModel

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/register")
def register(user_data: RegisterModel):
    print(user_data)
    return {"message": "Registered Successfully!"}


@auth_router.post("/login")
def login(user_data: LoginModel):
    if user_data:
        return {"message": "Login Successfully!"}
