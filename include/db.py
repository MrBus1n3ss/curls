import sqlite3


class DB_Connect:

    def __init__(self):
        self.connection = sqlite3.connect('curls.db')
        self.cursor = self.connection.cursor()

    def check_db(self):
        return self.connection.total_changes

    def get_tables(self):
        data = self.cursor.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        return data.fetchall()
