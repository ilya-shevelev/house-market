from src.config.verify_code import verify_code_config
from src.domain.user.dtos import VerifyCodeDTO
from src.infra.redis.dependencies import INoSQL


class VerifyCodeRepository:
	prefix = "verify"
	ttl = verify_code_config.TTL

	def __init__(self, nosql: INoSQL) -> None:
		self.nosql = nosql

	async def create(self, dto: VerifyCodeDTO) -> None:
		await self.nosql.set(dto.user_id, dto.code, self.ttl, self.prefix)
