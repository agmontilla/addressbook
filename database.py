import sqlite3


class DataBase:
    def __init__(self, database_name="prueba.db"):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self._create_adress_book()

    def _create_adress_book(self):
        sql = "CREATE TABLE IF NOT EXISTS addressbook ( \
            id INTEGER PRIMARY KEY, \
            first_name TEXT NOT NULL, \
            last_name TEXT NOT NULL, \
            cell_phone_number VARCHAR(13) NOT NULL \
            )"

        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, register):
        sql = "INSERT INTO addressbook (first_name, last_name, cell_phone_number) VALUES (?, ?, ?)"

        self.cursor.execute(sql, register)
        self.connection.commit()

    def delete(self, idx):
        sql = "DELETE FROM addressbook WHERE id=?"

        self.cursor.execute(sql, (idx,))
        self.connection.commit()

    def update(self, column_name, idx):
        sql = "UPDATE addressbook SET {} WHERE id=?".format(column_name)

        self.cursor.execute(sql, (idx,))
        self.connection.commit()
