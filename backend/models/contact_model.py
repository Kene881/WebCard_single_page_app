from sqlalchemy import Column, String, Integer

from database import Base


class ContactModel(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=True)
    email = Column(String(256), unique=True, nullable=False)
    description = Column(String(256), nullable=True)
