from src.addressbook.domain.contact import AddressDetails
from src.addressbook.domain.contact import Contact
from src.addressbook.domain.contact import PersonalInformation


class TestContact:
    def test_create_contact_works(self) -> None:
        addr = AddressDetails(
            street="1234 Main St",
            city="Springfield",
            state="IL",
            zip_code="62701",
        )
        personal_info = PersonalInformation(
            first_name="John",
            last_name="Doe",
            nickname="JD",
        )
        contact = Contact(
            personal_info=personal_info,
            address=addr,
            phone_number="555-555-5555",
            email_address="jhondoe@example.com",
        )

        assert contact.id is not None
        assert contact.personal_info == personal_info
        assert contact.address == addr
        assert contact.phone_number == "555-555-5555"
        assert contact.email_address == "jhondoe@example.com"
