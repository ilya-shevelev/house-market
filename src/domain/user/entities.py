from dataclasses import dataclass
from enum import Enum
from uuid import UUID

from argon2 import PasswordHasher


class Role(Enum):
	USER = "USER"
	REALTOR = "REALTOR"
	ADMIN = "ADMIN"
	SUPERUSER = "SUPERUSER"


@dataclass(frozen=True)
class User:
	first_name: str
	last_name: str
	username: str
	email: str
	role_id: UUID
	password: str | None = None

	def hash_password(self, password: str, hasher=PasswordHasher()) -> str:
		hashed = hasher.hash(password.encode("utf-8"))
		return hashed
