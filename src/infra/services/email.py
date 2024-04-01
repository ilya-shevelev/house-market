from email.mime.text import MIMEText


from src.config.email import email_config
from src.domain.user.dtos import EmailDTO
from src.infra.tasks.send_email import send_email


class EmailService:
	def __init__(self) -> None:
		self.user = email_config.USER
		self.password = email_config.PASSWORD
		self.smtp_port = email_config.PORT
		self.smtp_host = email_config.HOST

	async def send_email(self, dto: EmailDTO) -> None:
		message = MIMEText(dto.body)
		message["Subject"] = dto.subject
		message["From"] = self.user
		message["To"] = dto.recipient_email

		await send_email(
			message,
			self.user,
			self.password,
			self.smtp_host,
			self.smtp_port,
			dto.recipient_email,
		)


email_service = EmailService()
