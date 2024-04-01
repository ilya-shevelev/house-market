from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.session_factory import session_factory

ISession = Annotated[AsyncSession, Depends(session_factory.get_session)]
