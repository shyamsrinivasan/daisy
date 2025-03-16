import jwt
import datetime
import uuid

from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2
from sqlmodel import Session

from passlib.context import CryptContext
from typing import Dict, Any

from core.database import get_db
from core.config import CoreConfig
from core.utils.redis import RedisUtil


class AuthHandler:
    security = HTTPBearer()
    # security = OAuth2()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = 'erfjdsirmduwu4748djskwm38728dj'

    def hash_password(self, password):
        return self.pwd_context.hash(password)
    
    def verify_password(self, password, hashed_password):
        return self.pwd_context.verify(password, hashed_password)
    
    @staticmethod
    async def write_to_redis(key: str, value: Any):
        await RedisUtil.save_to_redis(key, value)

    @staticmethod
    async def read_from_redis(key: str):
        return await RedisUtil.get_from_redis(key)
    
    def encode_token(self, user_info: Dict):
        payload = {
            'exp': (datetime.datetime.now(datetime.timezone.utc) + 
                       datetime.timedelta(hours=CoreConfig.ACCESS_TOKEN_EXPIRE_MINUTES)),
            'iat': datetime.datetime.now(datetime.timezone.utc),
            'user_name': user_info['username'],            
            'session_id': user_info['session_id'],
        }
        return jwt.encode(payload, self.secret, algorithm='HS256')
    
    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret, algorithms='HS256')
            return payload['username'] , uuid.UUID(payload['session_id'])
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Expired Signature')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Token')
        
    async def get_current_user(self, auth: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
        try:
            # read user details from redis
            user_details = await self.read_from_redis(auth.credentials)
            (user_name, session_id) = self.decode_token(auth.credentials)            
        except HTTPException as e:
            raise e
        return user_name, user_details['user_id']


def auth_instance():
    return AuthHandler()