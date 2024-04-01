from uuid import UUID

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.lib.models import Base


class UserModel(Base):
	"""
	Модель пользователя

	:param first_name: Имя пользователя
	:param last_name: Фамилия пользователя
	:param username: Логин пользователя
	:param password: Пароль пользователя
	:param email: Электронная почта пользователя
	:param role_id: ID роли пользователя
	:param role: Роль пользователя
	:param customer_profile: Профиль пользователя как покупателя/арендатора
	:param seller_profile: Профиль пользователя как продавца/арендодателя
	:param realtor_profile: Профиль пользователя как риелтора
	:param subscriptions: Список подписок (тех пользователей, на которых подписан этот)
	:param subscribers: Список подписчиков (тех пользователей, которые подписаны на этого)
	"""

	__tablename__ = "users"

	first_name: Mapped[str] = mapped_column(String(20), nullable=True)
	last_name: Mapped[str] = mapped_column(String(20), nullable=True)
	username: Mapped[str] = mapped_column(String(20), unique=True)
	password: Mapped[str]
	email: Mapped[str] = mapped_column(String(50), unique=True)
	role_id: Mapped[UUID] = mapped_column(ForeignKey("roles.id"))

	role: Mapped["RoleModel"] = relationship("RoleModel", back_populates="users")  # noqa: F821
	customer_profile = relationship(
		"CustomerProfile", uselist=False, back_populates="user"
	)
	seller_profile = relationship("SellerProfile", uselist=False, back_populates="user")
	realtor_profile = relationship(
		"RealtorProfile", uselist=False, back_populates="user"
	)
	subscriptions: Mapped[list["UserModel"]] = relationship(
		"User",
		secondary="subscriptions",
		primaryjoin="User.id==Subscription.subscriber_id",
		secondaryjoin="User.id==Subscription.subscribed_id",
		backref="subscribers",
	)
	subscribers: Mapped[list["UserModel"]] = relationship(
		"User",
		secondary="subscriptions",
		primaryjoin="User.id==Subscription.subscribed_id",
		secondaryjoin="User.id==Subscription.subscriber_id",
		backref="subscriptions",
	)
