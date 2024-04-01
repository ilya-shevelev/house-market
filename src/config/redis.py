from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisConfig(BaseSettings):
	HOST: str
	PORT: int
	PASSWORD: str
	DB: int

	model_config = SettingsConfigDict(env_prefix="REDIS_")


redis_config = RedisConfig()
