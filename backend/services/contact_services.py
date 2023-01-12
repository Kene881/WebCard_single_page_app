from sqlalchemy.ext.asyncio import AsyncSession

from respositories.contact_repository import create_contact, get_contacts
from schemas.contact_schemas import ContactIn
from models.contact_model import ContactModel


async def get_contacts_service(session: AsyncSession):
    contacts_from_db = await get_contacts(session)
    return contacts_from_db


async def create_contact_service(session: AsyncSession, contact: ContactIn):
    db_contact = ContactModel(
        name=contact.name,
        email=contact.email,
        description=contact.description,
    )
    contact = await create_contact(session, db_contact)
    return contact
