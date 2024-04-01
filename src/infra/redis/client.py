import json

from aioredis import Redis

from src.config.redis import redis_config


class RedisClient:
	def __init__(
		self,
		host=redis_config.HOST,
		port=redis_config.PORT,
		db=redis_config.DB,
		password=redis_config.PASSWORD,
	) -> None:
		self.conn = Redis(host=host, port=port, db=db, password=password)

	async def get(self, key: str) -> str:
		value = await self.conn.get(key)
		if value:
			return json.loads(value)

	async def set(
		self, key: str, value: str, ttl: int | None = None, prefix: str | None = None
	) -> None:
		if prefix:
			key = f"{prefix}:{key}"
		value = json.dumps(value)
		await self.conn.set(key, value, ex=ttl)
