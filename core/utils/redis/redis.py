import json

import redis

from typing import Any

from core.config import CoreConfig, RedisConfig


class RedisUtil:
    client = redis.Redis(host=RedisConfig.REDIS_HOST, 
                        port=RedisConfig.REDIS_PORT,
                        username=RedisConfig.REDIS_USER,
                        password=RedisConfig.REDIS_PASS,
                        decode_responses=True)
    
    @classmethod
    async def save_to_redis(cls, key: str, value: Any) -> None:
        if not isinstance(value, str):
            value = json.dumps(value)
        expiry = CoreConfig.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        cls.client.set(key, value, ex=expiry)

    @classmethod
    def get_from_redis(cls, key: str) -> Any:
        value = cls.client.get(key)
        return json.loads(value) if value else None
