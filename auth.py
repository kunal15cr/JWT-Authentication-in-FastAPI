from datetime import datetime, timedelta, timezone
from authlib.jose import jwt, JWTError
from fastapi import HTTPException

# constants
SECRET_KEY = "my_secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Function to create a JWT token

def create_access_token(data: dict):
    header = {"alg" : ALGORITHM}
    expire = datetime.now(timezone.utc) + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = data.copy()
    payload.update({"exp": expire})
    return jwt.encode(header, payload, SECRET_KEY).decode('utf-8')

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY)
        payload.validate_exp()
        user_name = payload.get("sub")
        if user_name is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")