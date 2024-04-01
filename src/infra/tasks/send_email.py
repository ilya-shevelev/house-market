from email.mime.text import MIMEText

import celery
import aiosmtplib


@celery.task
async def send_email(
	message: MIMEText,
	user: str,
	password: str,
	host: str,
	port: int,
	recipient_email: str,
) -> None:
	await aiosmtplib.send(
		message.as_string(),
		sender=user,
		recipients=recipient_email,
		hostname=host,
		port=port,
		username=user,
		password=password,
	)
