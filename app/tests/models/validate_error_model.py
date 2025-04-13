from pydantic import BaseModel
from app.models.response_model import ErrorResponse


class ErrorResponse(BaseModel):
    detail: ErrorResponse
