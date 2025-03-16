from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.params import Depends
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_200_OK
from sqlmodel import Session

from core.auth import AuthHandler, auth_instance
from schemas.core.responses import ResponseModel

from core.database import get_db
from core.config import CoreConfig
from core.constants import MessageEN

from schemas.user import UserLogin, UserAdd

from repos.user import user_from_username, add_new_user, login


router = APIRouter(tags=['user'])
# auth_handler = AuthHandler()

@router.post('/login', tags=['login'], description='User login', 
            response_model=ResponseModel)
async def user_login(user: UserLogin, db: Session = Depends(get_db), 
                    auth: AuthHandler = Depends(auth_instance)):
    response = await login(user, auth, db)
    # user_obj = await user_from_username(user.username, db)
    # if not user_obj:
    #     response = ResponseModel(status=404, message='Invalid Username or Password')
    #     return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)
    # verified = auth.verify_password(user.password, user_obj.PasswordHash)
    # if not verified:
    #     response = ResponseModel(status=404, message='Invalid Username or Password')
    #     return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)    
    # # user details
    # # encode token    
    # token = auth.encode_token(user_obj.UserName, user_obj.UserId)
    # response = ResponseModel(data=jsonable_encoder({'token': token, 'user_details': []}))
    return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)    


@router.post('/add', tags=['add'], description='Add new user', 
            response_model=ResponseModel)
async def add_user(user_add: UserAdd, db: Session = Depends(get_db), 
                   auth: AuthHandler = Depends(auth_instance)):      
    response = await add_new_user(user_add, auth, db)
    return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)   
 