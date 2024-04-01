from typing import Annotated

from fastapi import Depends

from src.infra.redis.client import RedisClient


INoSQL = Annotated[RedisClient, Depends(RedisClient)]
