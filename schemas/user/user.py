from sqlmodel import SQLModel
from typing import Optional


class UserAdd(SQLModel):
    UserName: str    
    FirstName: str
    LastName: Optional[str] = None
    Email: str


class UserLogin(SQLModel):
    Domain: str
    Username: str
    Password: str
    DeviceId: Optional[str] = None


class LoginReturn(SQLModel):
    token: Optional[str] = None
    UserName: str
    FirstName: str
    LastName: Optional[str] = None
    UserImage: Optional[str] = None
    