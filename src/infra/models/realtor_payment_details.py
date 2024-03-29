from uuid import UUID

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.lib.models import Base


class RealtorPaymentDetailsModel(Base):
	"""
	Платежные реквизиты риелтора

	:param card_number: Номер карты (XXXX XXXX XXXX XXXX)
	:param profile_id: ID профиля риелтора
	"""

	__tablename__ = "realtor_payment_details"

	card_number: Mapped[str] = mapped_column(String(16), unique=True)
	profile_id: Mapped[UUID] = mapped_column(ForeignKey("realtor_profiles.id"))

	profile = relationship("RealtorProfile", back_populates="payment_details")
