from sqlmodel import SQLModel
from typing import Optional, Any


class ResponseModel(SQLModel):
    data: Optional[Any] = []
    status: int = 200
    message: Optional[str] = 'OK'
    