from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.lib.models import Base


class RealtorProfileModel(Base):
	"""
	Профиль пользователя как риелтора

	:param user_id: ID пользователя
	"""

	__tablename__ = "realtor_profiles"

	user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=True)

	user = relationship("User", back_populates="realtor_profile")
	payment_details = relationship(
		"RealtorPaymentDetails", uselist=False, back_populates="profile"
	)
