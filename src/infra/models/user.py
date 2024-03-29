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
    """

    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(String(20))
    last_name: Mapped[str] = mapped_column(String(20))
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(String(50), unique=True)
    role_id: Mapped[UUID] = mapped_column(ForeignKey("roles.id"))

    role: Mapped["RoleModel"] = relationship("RoleModel", back_populates="users")
