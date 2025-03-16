from sqlmodel import SQLModel
from typing import Optional, Any


class ResponseModel(SQLModel):
    data: Optional[Any] = []
    status: int = 200
    message: Optional[str] = 'OK'


class UnAuthorized(ResponseModel):
    status: int = 401
    message: str = 'User unauthorized'


response_dict = {
    200: { "model": ResponseModel },
    401: { "model": UnAuthorized },
}