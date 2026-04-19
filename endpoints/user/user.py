from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.params import Depends
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session
from typing import Dict

from fastapi_versioning import version

from core.auth import AuthHandler, auth_instance
from schemas.core.responses import ResponseModel, UnAuthorized, response_dict

from core.database import get_db
from core.config import CoreConfig
from core.constants import MessageEN

from schemas.user import UserLogin, UserAdd

from repos.user import user_from_username, add_new_user, login


router = APIRouter(tags=['user'])
auth = AuthHandler()

@router.post('/login', tags=['login'], description='User login', 
            response_model=ResponseModel)
@version(1)
async def user_login(user: UserLogin, db: Session = Depends(get_db), 
                    auth: AuthHandler = Depends(auth_instance)):
    response = await login(user, auth, db)
    return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)    


@router.post('/add', tags=['add'], description='Add new user', 
            responses=response_dict)
@version(1)
async def add_user(user_add: UserAdd, db: Session = Depends(get_db), 
                   auth: AuthHandler = Depends(auth_instance),
                   user: Dict = Depends(auth.current_user)):    
    if user:  
        print(f'user details: {user}\n')
        response = await add_new_user(user_add, auth, user['user_id'], db)
        return JSONResponse(jsonable_encoder(response), status_code=status.HTTP_200_OK)   
    return JSONResponse(jsonable_encoder(UnAuthorized()), status_code=status.HTTP_401_UNAUTHORIZED)
    
 