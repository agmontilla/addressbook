from src.addressbook import AddressBook
from src.database import DataBase

if __name__ == "__main__":
    db = DataBase()
    addbook = AddressBook(db)

    members = [
        ("Alfonso", "Montilla", "11111111"),
        ("Lizbeth", "Molina", "2222222"),
    ]

    addbook.add(members)
