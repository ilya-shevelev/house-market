from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
	POSTGRES_USER: str
	POSTGRES_PASSWORD: str
	POSTGRES_HOST: str
	POSTGRES_PORT: str
	POSTGRES_DB: str

	@property
	def database_url(self) -> PostgresDsn | None:
		return (
			f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
			f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
		)


database_config = DatabaseConfig()
