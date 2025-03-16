import uuid
import datetime

from sqlmodel import Session, select
from fastapi.encoders import jsonable_encoder

from automapper import mapper

from core.config import CoreConfig
from core.auth import AuthHandler
from core.constants import MessageEN

from core.models import User

from schemas.core.responses import ResponseModel
from schemas.user import UserAdd, UserLogin, LoginReturn


async def user_from_username(username: str, db: Session) -> User | None:
    query = select(User).where(User.NormalizedUserName == username.upper(), 
                               User.IsActive == True)
    return db.exec(query).first()


async def user_from_email(email: str, db: Session) -> User | None:
    query = select(User).where(User.NormalizedEmail == email.upper(), 
                               User.IsActive == True)
    return db.exec(query).first()


async def login(data: UserLogin, 
                auth: AuthHandler, 
                db: Session) -> ResponseModel:
    user_obj = await user_from_username(data.Username, db)
    if not user_obj:        
        return ResponseModel(status=400, message=MessageEN.auth_fail)
    verified = auth.verify_password(data.Password, user_obj.PasswordHash)
    if not verified:
        return ResponseModel(status=400, message=MessageEN.auth_fail)
    
    # get misc user details and store as dict      
    user_details = {
        'session_id': str(uuid.uuid4()),
        'username': user_obj.UserName,
        'email': user_obj.Email,
        'user_id': str(user_obj.UserId),
    }       

    # encode token    
    token = auth.encode_token(user_details)
    
    # write user details to redis memory with token as key
    await auth.write_to_redis(token, user_details)    

    # return login data
    user_data = mapper.to(LoginReturn).map(user_obj)
    user_data.token = token    
    return ResponseModel(data=jsonable_encoder(user_data), message=MessageEN.login_success)


async def add_new_user(user_add: UserAdd, auth: AuthHandler, 
                       user_id: uuid.UUID,
                       db: Session) -> ResponseModel:
    
    user_obj = mapper.to(User).map(user_add)
    existing_user = await user_from_username(user_add.UserName, db)
    if existing_user:
        return ResponseModel(status=400, message=MessageEN.username_exists)
    
    existing_user = await user_from_email(user_add.Email, db)
    if existing_user:
        return ResponseModel(status=400, message=MessageEN.useremail_exists)    
    
    user_obj.PasswordHash = auth.hash_password(CoreConfig.DEFAULT_USER_PASSWORD)
    user_obj.NormalizedUserName = user_obj.UserName.upper()
    user_obj.NormalizedEmail = user_obj.Email.upper()
    user_obj.CreatedBy = user_id
    user_obj.CreatedDate = datetime.datetime.now()
    user_obj.IsActive = True
    db.add(user_obj)
    db.commit()    
    return ResponseModel(message=MessageEN.user_add_success)
    