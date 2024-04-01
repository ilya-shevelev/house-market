from string import digits

from pydantic_settings import BaseSettings, SettingsConfigDict


class VerifyCodeConfig(BaseSettings):
	LENGTH: int
	VALID_CHARACTERS: str = digits

	model_config = SettingsConfigDict(env_prefix="VERIFY_CODE_")


verify_code_config = VerifyCodeConfig()
