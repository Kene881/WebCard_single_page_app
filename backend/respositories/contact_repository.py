from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from models.contact_model import ContactModel


async def get_contacts(session: AsyncSession):
    stmt = text("""
        select * from contacts;
    """)
    contacts = await session.execute(stmt)
    return contacts.all()


async def create_contact(session: AsyncSession, contact: ContactModel):
    async with session.begin():
        session.add(contact)
        await session.flush()
    await session.refresh(contact)
    return contact
