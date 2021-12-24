from db_config import with_database
import sqlite3


class DatabaseResponse:
    error: str
    data: list

    def __init__(self, data: list = None, error: str = None) -> None:
        self.error = error
        self.data = data

    def isOk(self):
        return self.error == None or len(self.error) == 0


@with_database
def perform_query(connection: sqlite3.Connection, query: str):
    try:
        data = connection.cursor().execute(query).fetchall()
        return DatabaseResponse(data)
    except sqlite3.Error as e:
        return DatabaseResponse(error=str(e))
