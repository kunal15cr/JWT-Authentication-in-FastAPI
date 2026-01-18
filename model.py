from pydantic import BaseModel, Field
from typing import List, Optional

class User(BaseModel):
    username: str
    password: str

class UserInDB(User):
    hashed_password: str