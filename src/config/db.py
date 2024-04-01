from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
	USER: str
	PASSWORD: str
	HOST: str
	PORT: str
	DB: str
	ECHO: bool = False

	model_config = SettingsConfigDict(env_prefix="POSTGRES_")

	@property
	def database_url(self) -> PostgresDsn | None:
		return (
			f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
			f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
		)


db_config = DatabaseConfig()
