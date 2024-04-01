from typing import Generator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config.db import db_config


class DatabaseSessionFactory:
	def __init__(self, url: str, echo: bool) -> None:
		self.engine = create_async_engine(url, echo=echo)
		self.session_factory = async_sessionmaker(
			self.engine, expire_on_commit=False, autoflush=False, autocommit=False
		)

	async def get_session(self) -> Generator[AsyncSession, None, None] | None:
		from sqlalchemy.exc import SQLAlchemyError

		session = self.session_factory()
		try:
			yield session
		except SQLAlchemyError:
			await session.rollback()
			raise
		finally:
			await session.close()


session_factory = DatabaseSessionFactory(db_config.database_url, db_config.ECHO)
