from fastapi import Request, HTTPException
from jose import jwt, JWTError
from datetime import datetime
from fastapi.responses import JSONResponse

SECRET_KEY = "zeeboombhaa"
ALGORITHM = "HS256"


async def jwt_middleware(request: Request, call_next):
    # List of routes to skip
    excluded_paths = ["/auth/login", "/auth/register", "/public", "/health-check"]

    if request.url.path in excluded_paths:
        # If the path is excluded, skip the JWT verification
        response = await call_next(request)
        return response

    # If the path is not excluded, validate the token
    token = request.cookies.get("token")

    if not token:
        # Handle missing token gracefully by returning 401 Unauthorized
        return JSONResponse(status_code=401, content={"detail": "Token not found"})

    try:
        # Decode the token to verify it's valid
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        request.state.user = payload  # Store the user info in the request state
    except JWTError:
        # Handle invalid token
        return JSONResponse(status_code=401, content={"detail": "Invalid token"})

    # Process the request as normal
    response = await call_next(request)
    return response
