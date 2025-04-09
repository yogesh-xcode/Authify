import bcrypt
from app.schemas.auth_schemas import User


def hashpw(passwd: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passwd.encode(), salt)
    return hashed.decode()


def checkpw(passwd: str, hashed_pw: str) -> bool:
    # Encode both for bcrypt to work
    return bcrypt.checkpw(passwd.encode(), hashed_pw.encode())
