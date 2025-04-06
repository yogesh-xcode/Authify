from typing import Union
from tortoise.exceptions import IntegrityError
from app.schemas.auth_schemas import User
from app.core.crypto.hashing import hashpw, checkpw


# ✅ Check if user email or username already exists
async def user_exist(user: dict) -> bool:
    email_exist = await User.filter(email=user["email"]).exists()
    uname_exist = await User.filter(username=user["username"]).exists()
    return email_exist or uname_exist


# ✅ Create a new user if not already registered
async def create_user(user: dict) -> Union[dict, str]:
    exists = await user_exist(user)  # ⛔ Avoid shadowing the function name
    if exists:
        return "user email/username already exists"

    try:
        user["password"] = hashpw(str(user["password"]))  # Hash the password
        new_user = await User.create(**user)

        return (
            await User.filter(email=new_user.email).values("id", "username", "email")
        )[0]

    except IntegrityError:
        return "user creation failed due to database error"


# ✅ Validate user login
async def validate_user(user: dict) -> bool:
    result = await User.filter(email=user["email"]).values("password")

    if not result:
        return False

    stored_hash = result[0]["password"]
    return checkpw(passwd=user["passwd"], hashed=stored_hash)
