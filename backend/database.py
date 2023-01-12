from typing import AsyncIterator

from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from configs import SQL_ALCHEMY_DB_URL

# docker run --name testdbmywebcard -p 5432:5432 -e POSTGRES_USER=pguser -e POSTGRES_PASSWORD=pgkalmatmlgh3032810 -e POSTGRES_DB=webcard -d postgres:15-alpine

async_engine = create_async_engine(SQL_ALCHEMY_DB_URL)

async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession
)

Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
