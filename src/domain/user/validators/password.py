from src.config.password import password_config
from src.domain.user.exceptions import IncompletePassword, InvalidPassword


class PasswordValidator:
	@classmethod
	def validate(cls, password: str) -> None:
		cls.validate_incomplete_password(password)
		cls.validate_invalid_characters(password)

	@staticmethod
	def validate_incomplete_password(password: str) -> None:
		is_upper = any(char.isupper() for char in password)
		is_lower = any(char.islower() for char in password)
		if (
			password.isdigit()
			or not (is_lower and is_upper)
			or password.isalnum()
			or not any(char.isdigit() for char in password)
		):
			raise IncompletePassword(
				"Password must contain at least one digit, one letter each in lower and upper case and one special character."
			)

	@staticmethod
	def validate_invalid_characters(
		self, password: str, config=password_config
	) -> None:
		if not all(character in config.VALID_CHARACTERS for character in password):
			raise InvalidPassword("Password contains invalid characters.")
