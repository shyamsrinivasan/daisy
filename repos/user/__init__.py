from sqlmodel import Session, select

from automapper import mapper

import uuid
import datetime

from core.config import CoreConfig
from core.auth import AuthHandler

from core.models import User

from schemas.user import UserAdd


async def user_from_username(username: str, db: Session):
    query = select(User).where(User.NormalizedUserName == username.upper(), User.IsActive == True)
    return db.exec(query).first()


async def user_from_email(email: str, db: Session):
    query = select(User).where(User.NormalizedEmail == email.upper(), User.IsActive == True)
    return db.exec(query).first()


async def add_new_user(user_add: UserAdd, db: Session) -> User | int:
    auth_handler = AuthHandler()
    user_obj = mapper.to(User).map(user_add)
    existing_user = await user_from_username(user_add.UserName, db)
    if existing_user:
        return 1
    existing_user = await user_from_email(user_add.Email, db)
    if existing_user:
        return 2
    user_obj.UserId = uuid.uuid4()
    user_obj.PasswordHash = auth_handler.hash_password(CoreConfig.DEFAULT_USER_PASSWORD)
    user_obj.NormalizedUserName = user_obj.UserName.upper()
    user_obj.NormalizedEmail = user_obj.Email.upper()
    user_obj.CreatedDate = datetime.datetime.now()
    user_obj.IsActive = True
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj