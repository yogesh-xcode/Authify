from pydantic import BaseModel, Field, EmailStr


class BaseAuthModel(BaseModel):
    email: EmailStr = Field(
        ..., description="Email of a user", examples=["ayathajm@gmail.com"]
    )
    password: str = Field(
        ...,
        min_length=7,
        max_length=20,
        description="Password of a user",
        examples=["aythu04sL"],
    )


class LoginModel(BaseAuthModel):
    pass


class RegisterModel(BaseAuthModel):
    username: str = Field(
        ...,
        min_length=7,
        max_length=15,
        description="username of a user",
        examples=["ayath.us"],
    )
