from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.lib.models import Base


class CustomerProfileModel(Base):
	"""
	Профиль пользователя как покупателя/арендатора

	:param user_id: ID пользователя
	"""

	__tablename__ = "customer_profiles"

	user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))

	user = relationship("User", back_populates="customer_profile")
