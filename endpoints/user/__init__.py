from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.params import Depends
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_200_OK
from sqlmodel import Session

from core.auth import AuthHandler
from schemas.core import ResponseModel

from core.database import get_db
from core.config import CoreConfig

from schemas.user import UserLogin, UserAdd

from repos.user import user_from_username, add_new_user


router = APIRouter()
auth_handler = AuthHandler()

@router.post('/login', tags=['user', 'login'], description='User login', response_model=ResponseModel)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    user_obj = await user_from_username(user.username, db)
    if not user_obj:
        response = ResponseModel(status=404, message='Invalid Username or Password')
        return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)
    verified = auth_handler.verify_password(user.password, user_obj.PasswordHash)
    if not verified:
        response = ResponseModel(status=404, message='Invalid Username or Password')
        return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)    
    # user details
    # encode token    
    token = auth_handler.encode_token(user_obj.UserName, user_obj.UserId)
    response = ResponseModel(data=jsonable_encoder({'token': token, 'user_details': []}))
    return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)    


@router.post('/add', tags=['user', 'add'], description='Add new user', response_model=ResponseModel)
async def add_user(user_add: UserAdd, db: Session = Depends(get_db)):      
    new_user_obj = await add_new_user(user_add, db)
    if new_user_obj == 1:
        response = ResponseModel(status=400, message='Username already exists')
        return JSONResponse(jsonable_encoder(response), status_code=HTTP_200_OK)
    if new_user_obj == 2:
        response = ResponseModel(status=400, message='User email already exists')
        return JSONResponse(jsonable_encoder(response), status_code=HTTP_200_OK)
    response = ResponseModel(data=jsonable_encoder(new_user_obj))
    return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)   
 