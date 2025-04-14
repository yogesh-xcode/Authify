from pydantic import BaseModel
from typing import List, Literal

from app.schemas.type_schema import UserData


# Success Response Model
class BaseDataModel(BaseModel):
    reason: str


class RegisterData(BaseDataModel):
    user_data: UserData


class SuccessResponse(BaseModel):
    success: Literal[True]
    message: str
    data: RegisterData


# Error Response Model
class Ctx(BaseModel):
    reason: str


class ErrorResponse(BaseModel):
    type: Literal["unauthorized_error", "conflict_error", "integrity_error"]
    loc: List[str]
    msg: str
    input: List[str]
    ctx: Ctx
