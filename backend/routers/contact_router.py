from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Body, Depends, status

from database import get_session
from schemas.contact_schemas import ContactIn, Contact
from services import contact_services

contact_router = APIRouter()


@contact_router.get(
    '/api/contacts',
    response_model=list[Contact]
)
async def get_contacts(session: AsyncSession = Depends(get_session)):
    contacts = await contact_services.get_contacts(session)
    return contacts


@contact_router.post(
    '/api/contact/create',
    status_code=status.HTTP_201_CREATED
)
async def create_contact(contact: ContactIn = Body(), session: AsyncSession = Depends(get_session)):
    await contact_services.create_contact_service(session, contact)
    return {"success": True}
