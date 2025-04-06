from fastapi import APIRouter, Body, Response
from starlette import status
from app.models.auth_model import RegisterModel, LoginModel
from app.services.auth_service import create_user


auth_router = APIRouter(prefix="/auth", tags=["Authentication routes"])


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_data: RegisterModel = Body(...), response: Response = Response()
):
    user = user_data.model_dump()
    user_created = await create_user(user)
    if isinstance(user_created, str):
        response.status_code = status.HTTP_400_BAD_REQUEST

    return user_created


@auth_router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login(user_data: LoginModel = Body(...)):
    return {"message": "Login Successfully!"}
