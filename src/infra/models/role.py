from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.user.entities import Role
from src.lib.models import Base


class RoleModel(Base):
	"""
	Модель роли пользователя

	:param code: Кодовое название роли
	"""

	__tablename__ = "roles"

	code: Mapped[Role] = mapped_column(String(9), unique=True)

	users: Mapped[list["UserModel"]] = relationship("UserModel", back_populates="role")  # noqa: F821
	permissions: Mapped[list["PermissionModel"]] = relationship(  # noqa: F821
		"PermissionModel", secondary="roles_permissions", back_populates="roles"
	)
