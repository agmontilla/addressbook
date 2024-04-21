import sqlite3


class DataBase:
    """Database class to manage the database"""

    def __init__(self, database_name: str = "prueba.db") -> None:
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self._create_adress_book()

    def _create_adress_book(self) -> None:
        sql = "CREATE TABLE IF NOT EXISTS addressbook ( \
            id INTEGER PRIMARY KEY, \
            first_name TEXT NOT NULL, \
            last_name TEXT NOT NULL, \
            cell_phone_number VARCHAR(13) NOT NULL \
            )"

        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, register: tuple[str, str, str]) -> None:
        """Insert a record into the database

        This method insert a record into the addressbook table
        """
        sql = "INSERT INTO addressbook (first_name, last_name, cell_phone_number) VALUES (?, ?, ?)"

        self.cursor.execute(sql, register)
        self.connection.commit()

    def delete(self, idx: int) -> None:
        """Delete a record from the database by id

        Remeber this delete the record from the addressbook table
        """
        sql = "DELETE FROM addressbook WHERE id=?"

        self.cursor.execute(sql, (idx,))
        self.connection.commit()

    def update(self, column_name: str, idx: int) -> None:
        """Update a record from the database by id

        Remeber this update the record from the addressbook table
        """
        sql = f"UPDATE addressbook SET {column_name} WHERE id=?"

        self.cursor.execute(sql, (idx,))
        self.connection.commit()
