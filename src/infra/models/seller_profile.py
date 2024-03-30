from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.lib.models import Base


class SellerProfileModel(Base):
	"""
	Профиль пользователя как продавца/арендодателя

	:param user_id: ID пользователя
	"""

	__tablename__ = "seller_profiles"

	user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=True)
	user = relationship("User", back_populates="seller_profile")
	payment_details = relationship(
		"SellerPaymentDetails", uselist=False, back_populates="profile"
	)
