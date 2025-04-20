from datetime import timedelta
from fastapi import APIRouter, Body, Response, HTTPException
from starlette import status
from app.schemas.auth_schema import RegisterModel, LoginModel
from app.schemas.response_schema import ErrorResponse, SuccessResponse
from app.services.auth_service import create_user, validate_user
from app.services.jwt_service import set_token

auth_router = APIRouter(prefix="/auth", tags=["Authentication routes"])


@auth_router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=ErrorResponse | SuccessResponse,
)
async def register(user_data: RegisterModel = Body(...)):
    # convert a pydantic model to a dict
    user = await create_user(user_data.model_dump())
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
async def login(response: Response, user_data: LoginModel = Body(...)):
    user = await validate_user(user_data.model_dump())
    if isinstance(user, ErrorResponse):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=user.model_dump()
        )

    set_token(user_email=user_data.email, minutes=15, response=response)

    return user
