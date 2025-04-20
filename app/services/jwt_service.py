import datetime
from fastapi import Response
from jose import jwt

SECRET_KEY = "zeeboombhaa"
ALGORITHM = "HS256"


def create_token(user_email: str, expires_delta: datetime.timedelta):
    encode: dict[str, object] = {
        "sub": user_email,
        "exp": int(
            (datetime.datetime.now(datetime.timezone.utc) + expires_delta).timestamp()
        ),
    }

    return {
        "token": jwt.encode(encode, key=SECRET_KEY, algorithm=ALGORITHM),
        "expires_delta": expires_delta,
    }


def set_token(user_email: str, minutes: int, response: Response):
    expires_delta = datetime.timedelta(minutes=minutes)
    token_data = create_token(user_email=user_email, expires_delta=expires_delta)

    response.set_cookie(
        key="token",
        value=token_data["token"],
        httponly=True,
        samesite="lax",
        max_age=int(expires_delta.total_seconds()),
    )

    response.set_cookie(
        key="chk",
        value="pass",
        httponly=True,
        samesite="lax",
        max_age=int(expires_delta.total_seconds()),
    )
