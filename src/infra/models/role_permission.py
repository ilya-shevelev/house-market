from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.lib.models import Base


class RolePermissionModel(Base):
	"""
	Смежная таблица ролей и разрешений

	:param role_id: ID роли
	:param permission_id: ID разрешения
	"""

	__tablename__ = "roles_permissions"

	role_id: Mapped[UUID] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))
	permission_id: Mapped[UUID] = mapped_column(
		ForeignKey("permissions.id", ondelete="CASCADE")
	)
