from src.domain.user.dtos import VerifyCodeDTO


class VerifyCodeRepository:
	async def create(self, dto: VerifyCodeDTO) -> None: ...
