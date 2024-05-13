from src.base.domain.normalizers import to_capitalize


def test_to_capitalize_success() -> None:
    assert to_capitalize("john doe") == "John Doe"
    assert to_capitalize("john") == "John"
    assert to_capitalize("johN") == "John"
