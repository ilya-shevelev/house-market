from string import printable

from pydantic_settings import SettingsConfigDict, BaseSettings


class PasswordConfig(BaseSettings):
	MIN_LENGTH: int
	MAX_LENGTH: int
	VALID_CHARACTERS: str = printable

	model_config = SettingsConfigDict(env_prefix="PASSWORD_")


password_config = PasswordConfig()
