from typing import Annotated

from annotated_types import Len
from pydantic import EmailStr, AfterValidator

from src.config.password import password_config
from src.domain.user.validators.email import EmailValidator
from src.domain.user.validators.password import PasswordValidator

Email = Annotated[
	EmailStr,
	Len(min_length=7, max_length=50),
	AfterValidator(lambda x: EmailValidator.validate(x)),
]


Password = Annotated[
	str,
	Len(min_length=password_config.MIN_LENGTH, max_length=password_config.MAX_LENGTH),
	AfterValidator(lambda x: PasswordValidator.validate(x)),
]
