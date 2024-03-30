from uuid import UUID

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.lib.models import Base


class SellerPaymentDetailsModel(Base):
	"""
	Платежные реквизиты продавца

	:param card_number: Номер карты (XXXX XXXX XXXX XXXX)
	:param profile_id: ID профиля продавца
	"""

	__tablename__ = "seller_payment_details"

	card_number: Mapped[str] = mapped_column(String(16), unique=True)
	profile_id: Mapped[UUID] = mapped_column(ForeignKey("seller_profiles.id"))

	profile = relationship("SellerProfile", back_populates="payment_details")
