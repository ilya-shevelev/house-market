import re

from src.domain.user.exceptions import InvalidEmailCharacters, InvalidEmailDomain


class EmailValidator:
	@classmethod
	def validate(cls, email: str) -> None:
		cls.validate_characters(email)
		cls.validate_domain(email)

	@staticmethod
	def validate_characters(email: str) -> None:
		if not re.fullmatch(r"^[a-zA-Z0-9@'._-]*$", email):
			raise InvalidEmailCharacters(
				"Email must contain only latin characters, digits and punctuation."
			)

	@staticmethod
	def validate_domain(email: str) -> None:
		domain_name = email.split("@")[-1]
		for j in list(domain_name.split(".")):
			if len(j) < 2:
				raise InvalidEmailDomain("invalid domain part of the email.")
