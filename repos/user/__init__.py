from sqlmodel import Session, select

from core.models import User


async def user_from_username(username: str, db: Session):
    query = select(User).where(User.UserName == username, User.IsActive == True)
    return db.exec(query).first()
