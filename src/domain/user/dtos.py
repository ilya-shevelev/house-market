from uuid import UUID

from pydantic import model_validator, constr

from src.config.verify_code import verify_code_config
from src.domain.user.exceptions import MismatchedPasswords
from src.domain.user.types import Email, Password
from src.lib.dtos import BaseDTO


class UserDTO(BaseDTO):
	username: constr(max_length=20)
	email: Email


class UserCreateDTO(BaseDTO):
	username: constr(max_length=20)
	email: Email
	password: Password
	role_id: UUID


class UserRegisterDTO(BaseDTO):
	username: constr(max_length=20)
	email: Email
	password: Password
	password_confirm: Password

	@model_validator(mode="after")
	def fields_validate(self):
		if self.password != self.password_confirm:
			raise MismatchedPasswords("Passwords do not match.")
		return self


class EmailDTO(BaseDTO):
	email: Email
	subject: str
	body: str


class VerifyCodeDTO(BaseDTO):
	code: constr(
		min_length=verify_code_config.LENGTH, max_length=verify_code_config.LENGTH
	)
	user_id: UUID
