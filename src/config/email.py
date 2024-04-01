from pydantic_settings import BaseSettings, SettingsConfigDict


class EmailConfig(BaseSettings):
	USER: str
	PASSWORD: str
	HOST: str = "smtp.gmail.com"
	PORT: int = 465

	model_config = SettingsConfigDict(env_prefix="SMTP_")


email_config = EmailConfig()
