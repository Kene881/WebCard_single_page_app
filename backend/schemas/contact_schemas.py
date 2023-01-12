from pydantic import BaseModel, validator, EmailStr


class Contact(BaseModel):
    name: str
    email: EmailStr
    description: str

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True


class ContactIn(BaseModel):
    name: str
    email: EmailStr
    description: str

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True

    @validator("name")
    def name_is_not_empty(cls, v):
        if len(v) <= 0:
            raise ValueError("name is empty")
        return v
