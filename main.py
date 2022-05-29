from database import DataBase
from addressbook import AddressBook


if __name__ == "__main__":
    db = DataBase()
    addbook = AddressBook(db)

    members = [
        ("Alfonso", "Montilla", "11111111"),
        ("Lizbeth", "Molina", "2222222"),
    ]

    addbook.add(members)
