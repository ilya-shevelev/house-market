from typing import Annotated

from fastapi import Depends

from src.infra.repositories.role import RoleRepository
from src.infra.repositories.verify_code import VerifyCodeRepository
from src.infra.repositories.user import UserRepository
from src.infra.services.email import EmailService

IUserRepository = Annotated[UserRepository, Depends(UserRepository)]
IVerifyCodeRepository = Annotated[VerifyCodeRepository, Depends(VerifyCodeRepository)]
IEmailService = Annotated[EmailService, Depends(EmailService)]
IRoleRepository = Annotated[RoleRepository, Depends(RoleRepository)]
