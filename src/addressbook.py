from src.database import DataBase


class AddressBook:
    """Class that represents an address book"""

    def __init__(self, db: DataBase) -> None:
        self.db = db

    def add(self, members: list[tuple[str, str, str]]) -> None:
        """Add a member to the address book"""
        for member in members:
            self.db.insert(member)

    def remove(self, idx: int) -> None:
        """Remove a member from the address book"""
        self.db.delete(idx)

    def modify(self, idx: int) -> None:
        """Modify a member from the address book"""
        self.db.update("cell_phone_number", idx)
        self.db.update("cell_phone_number", idx)
        self.db.update("cell_phone_number", idx)
