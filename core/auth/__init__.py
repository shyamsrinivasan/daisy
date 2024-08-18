from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel import Session

from passlib.context import CryptContext
from typing import Dict
import jwt

import datetime

from core.database import get_db


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = ''

    def hash_password(self, password):
        return self.pwd_context.hash(password)
    
    def verify_password(self, password, hashed_password):
        return self.pwd_context.verify(password, hashed_password)
    
    def encode_token(self, user_info: Dict):
        payload = {
            'expiry': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),
            'iat': datetime.datetime.now(datetime.timezone.utc),
            'user_name': user_info['user_name'],
            'user_id': str(user_info['user_id']),
        }
        return jwt.encode(payload, self.secret, algorithm='HS256')
    
    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret, algorithms='HS256')
            return payload['user_name'], payload['user_id']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Expired Signature')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')
        
    async def get_current_user(self, auth: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
        try:
            (user_name, user_id) = self.decode_token(auth.credentials)
        except HTTPException as e:
            raise e
        return user_name, user_id
