import pytest
from pydantic import BaseModel

from src.base.domain.validators import Phone


class TestPhoneValidator:
    class PhoneModel(BaseModel):
        phone: Phone

    @pytest.mark.parametrize(
        "phone_number",
        [
            "555-555-5555",
            "5555555555",
            "(555) 555-5555",
            "+1 555-555-5555",
            "+1 (555) 555-5555",
            "+1 5555555555",
            "+1 (555) 5555555",
            "+1 555-5555555",
        ],
    )
    def test_phone_validator_sucess(self, phone_number: str) -> None:
        phone = self.PhoneModel(phone=phone_number)
        assert phone.phone == phone_number

    @pytest.mark.parametrize(
        "phone_number",
        [
            "555-555-5555 ext. 1234",
            "",
            "+48 504 203 260@@",
            "+48.504.203.260",
            "+55(123) 456-78-90-",
            "+55(123) - 456-78-90",
            "504.203.260",
            " ",
            "-",
            "()",
            "() + ()",
            "(21 7777",
            "+48 (21)",
            "+",
        ],
    )
    def test_phone_validator_failure(self, phone_number: str) -> None:
        with pytest.raises(ValueError):
            self.PhoneModel(phone=phone_number)
