from sqlmodel import SQLModel
from typing import Optional


class UserLogin(SQLModel):
    domain: str
    username: str
    password: str


class UserAdd(SQLModel):
    UserName: str    
    FirstName: str
    LastName: Optional[str] = None
    Email: str
    