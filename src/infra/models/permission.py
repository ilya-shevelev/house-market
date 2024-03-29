from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.lib.models import Base


class PermissionModel(Base):
	"""
	Модель разрешения

	:param code: Кодовое название разрешения
	"""

	__tablename__ = "permissions"

	code: Mapped[str] = mapped_column(String(20), unique=True)
	description: Mapped[str] = mapped_column(String(50), nullable=True)

	roles: Mapped[list["RoleModel"]] = relationship(  # noqa: F821
		"RoleModel", secondary="roles_permissions", back_populates="permissions"
	)
