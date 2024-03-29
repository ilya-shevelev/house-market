from uuid import UUID, uuid4
from datetime import datetime

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
	"""
	Базовая модель SqlAlchemy

	:param id: Идентификатор
	:param created_at: Дата создания
	:param updated_at: Дата обновления
	"""

	__abstract__ = True

	id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True, unique=True)
	created_at: Mapped[datetime] = mapped_column(
		TIMESTAMP(timezone=True), server_default=func.now()
	)
	updated_at: Mapped[datetime] = mapped_column(
		TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now()
	)
