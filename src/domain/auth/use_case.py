from src.domain.user.dependencies import (
	IUserRepository,
	IEmailService,
	IVerifyCodeRepository,
	IRoleRepository,
)
from src.domain.user.dtos import (
	UserCreateDTO,
	EmailDTO,
	UserDTO,
	VerifyCodeDTO,
	UserRegisterDTO,
)
from src.domain.user.entities import User, Role


class AuthUseCase:
	def __init__(
		self,
		user_repository: IUserRepository,
		verify_code_repository: IVerifyCodeRepository,
		role_repository: IRoleRepository,
		email_service: IEmailService,
	) -> None:
		self.user_repository = user_repository
		self.verify_code_repository = verify_code_repository
		self.role_repository = role_repository
		self.email_service = email_service

	async def register(self, dto: UserRegisterDTO) -> UserDTO:
		user = User(username=dto.username, email=dto.email, password=dto.password)
		user.hash_password()
		verify_code = user.create_verify_code()
		role_id = await self.role_repository.get_by_code(Role.USER).id
		user_id = await self.user_repository.create(
			UserCreateDTO(
				username=user.username,
				email=user.email,
				password=user.password,
				role_id=role_id,
			)
		).id
		await self.verify_code_repository.create(
			VerifyCodeDTO(  # TODO: Redis
				code=verify_code,
				user_id=user_id,
			)
		)
		await self.email_service.send_email(  # TODO: сделать темплейт с jinja2
			EmailDTO(email=dto.email, subject="spam", body="eggs")
		)
		return UserDTO(username=user.username, email=user.email)
