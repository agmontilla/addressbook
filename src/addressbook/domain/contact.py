from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field
from pydantic import field_validator

from src.base.domain.identifiers import Identifiable
from src.base.domain.normalizers import to_capitalize
from src.base.domain.validators import Phone


class PersonalInformation(BaseModel):
    first_name: str
    last_name: Optional[str]
    nickname: Optional[str]


class AddressDetails(BaseModel):
    street: str
    city: str = Field(min_length=3)
    state: str
    zip_code: str

    _normalize_city = field_validator("city")(to_capitalize)


class Contact(Identifiable):
    personal_info: PersonalInformation
    address: AddressDetails
    phone_number: Phone
    email_address: Optional[EmailStr]


class AddressBook(Identifiable):
    contacts: list[Contact] = []
