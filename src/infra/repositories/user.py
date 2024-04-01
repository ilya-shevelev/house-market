from src.domain.user.dtos import UserCreateDTO
from src.infra.database.dependencies import ISession
from src.infra.models.user import UserModel


class UserRepository:
	model = UserModel

	def __init__(self, session: ISession) -> None:
		self.session = session

	async def create(self, dto: UserCreateDTO):
		instance = self.model(**dto.model_dump())
		self.session.add(instance)
		await self.session.commit()
		await self.session.refresh(instance)
		return instance
