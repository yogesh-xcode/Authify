from pydantic import BaseModel
from app.schemas.response_schema import ErrorResponse


class ErrorResponse(BaseModel):
    detail: ErrorResponse
