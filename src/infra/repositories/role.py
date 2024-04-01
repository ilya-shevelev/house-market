from sqlalchemy import select

from src.domain.user.entities import Role
from src.infra.database.dependencies import ISession
from src.infra.models.role import RoleModel


class RoleRepository:
	model = RoleModel

	def __init__(self, session: ISession) -> None:
		self.session = session

	async def get_by_code(self, code: Role):
		stmt = select(self.model).filter_by(code=code)
		raw = await self.session.execute(stmt)
		return raw.scalar_one_or_none()
