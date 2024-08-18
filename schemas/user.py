from sqlmodel import SQLModel


class UserLogin(SQLModel):
    domain: str
    username: str
    password: str