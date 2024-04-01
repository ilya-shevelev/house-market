from dataclasses import dataclass
from enum import Enum
from random import choice
from uuid import UUID

from argon2 import PasswordHasher

from src.config.verify_code import verify_code_config


class Role(Enum):
	USER = "USER"
	REALTOR = "REALTOR"
	ADMIN = "ADMIN"
	SUPERUSER = "SUPERUSER"


@dataclass
class User:
	username: str
	email: str
	first_name: str | None = None
	last_name: str | None = None
	role_id: UUID | None = None
	password: str | None = None

	def hash_password(self, hasher=PasswordHasher()) -> None:
		self.password = hasher.hash(self.password.encode("utf-8"))

	@staticmethod
	def create_verify_code(
		length=verify_code_config.LENGTH, characters=verify_code_config.VALID_CHARACTERS
	) -> str:
		return "".join(choice(characters) for _ in range(length))
