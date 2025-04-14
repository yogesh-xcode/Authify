from typing import Union
from tortoise.exceptions import IntegrityError
from app.models.auth_model import User
from app.core.crypto.hashing import hashpw, checkpw
from app.schemas.response_schema import (
    ErrorResponse,
    Ctx,
    SuccessResponse,
    RegisterData,
)
from app.schemas.type_schema import UserData


# Create a new user if not already registered
async def create_user(user: dict) -> ErrorResponse | SuccessResponse:
    email_exist = await User.filter(email=user["email"]).exists()
    uname_exist = await User.filter(username=user["username"]).exists()

    if email_exist or uname_exist:
        return ErrorResponse(
            type="conflict_error",
            loc=["body", "email", "username"],
            msg="user was not created: because the email/username is already register by other",
            input=[user["username"], user["email"]],
            ctx=Ctx(reason="username or email id is already exist!"),
        )

    user["password"] = hashpw(str(user["password"]))  # Hash the password
    try:
        new_user = await User.create(**user)
        return SuccessResponse(
            success=True,
            message="user was created/registered successfully!",
            data=RegisterData(
                user_data=UserData(
                    id=new_user.id, username=new_user.username, email=new_user.email
                ),
                reason="user is created/registered successfully",
            ),
        )

    except IntegrityError:
        return ErrorResponse(
            type="integrity_error",
            loc=["body"],
            msg="database error: unexpected error while creating user",
            input=[],
            ctx=Ctx(reason="database - integrity error"),
        )


# Validate user login
async def validate_user(user: dict) -> ErrorResponse | SuccessResponse:
    user_record = await User.filter(email=user["email"]).values(
        "id", "username", "email", "password"
    )

    if not user_record:
        return ErrorResponse(
            type="unauthorized_error",
            loc=["body", "email"],
            msg="email is invalid: email does not exist",
            input=[user["email"]],
            ctx=Ctx(reason="email is invalid"),
        )

    hashed_pw = user_record[0]["password"]

    if not hashed_pw or not checkpw(passwd=user["password"], hashed_pw=hashed_pw):
        return ErrorResponse(
            type="unauthorized_error",
            loc=["body", "password"],
            msg="password is invalid: password does not match with email Id",
            input=["*********"],
            ctx=Ctx(reason="password is invalid"),
        )

    return SuccessResponse(
        success=True,
        message="user validation success",
        data=RegisterData(
            user_data=UserData(
                id=user_record[0]["id"],
                username=user_record[0]["username"],
                email=user_record[0]["email"],
            ),
            reason="user is validated/logged sucessfully",
        ),
    )
