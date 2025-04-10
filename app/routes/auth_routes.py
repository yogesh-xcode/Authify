from fastapi import APIRouter, Body, Response, HTTPException
from starlette import status
from app.models.auth_model import RegisterModel, LoginModel
from app.models.response_model import ErrorResponse, SuccessResponse
from app.services.auth_service import create_user, validate_user


auth_router = APIRouter(prefix="/auth", tags=["Authentication routes"])


@auth_router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=ErrorResponse | SuccessResponse,
)
async def register(user_data: RegisterModel = Body(...)):
    # convert a pydantic model to a dict
    user_data = user_data.model_dump()
    user = await create_user(user_data)
    if isinstance(user, ErrorResponse):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=user.model_dump()
        )
    return user


@auth_router.post(
    "/login",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ErrorResponse | SuccessResponse,
)
async def login(user_data: LoginModel = Body(...)):
    user = await validate_user(user_data.model_dump())
    if isinstance(user, ErrorResponse):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=user.model_dump()
        )

    return user
