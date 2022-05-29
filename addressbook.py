class AddressBook:
    def __init__(self, db):
        self.db = db

    def add(self, members):
        for member in members:
            self.db.insert(member)

    def remove(self, idx):
        self.db.delete(idx)

    def modify(self, idx):
        self.db.update("cell_phone_number", idx)
