from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.lib.models import Base


class SubscriptionModel(Base):
	"""
	Смежная таблица подписок

	:param subscriber_id: ID подписчика
	:param subscribed_id: ID подписанного
	"""

	__tablename__ = "subscriptions"

	subscriber_id: Mapped[UUID] = mapped_column(
		ForeignKey("users.id", ondelete="CASCADE")
	)
	subscribed_id: Mapped[UUID] = mapped_column(
		ForeignKey("users.id", ondelete="CASCADE")
	)
