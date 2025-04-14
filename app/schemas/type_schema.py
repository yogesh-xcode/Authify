from pydantic import BaseModel
from uuid import UUID


class UserData(BaseModel):
    id: UUID
    username: str
    email: str
