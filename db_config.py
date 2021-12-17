from os import path
from os import mkdir
import os
import sqlite3
from sqlite3 import Connection

basedir = path.abspath(path.dirname(__file__))
database_directory = path.join(basedir, "db")
if not os.path.exists(database_directory):
    mkdir(database_directory)
database_filename = "database.db"
database = path.join(database_directory, database_filename)


def get_db() -> Connection:
   return sqlite3.connect(database)

def with_database(func):
    def wrapper(*args, **kwargs):
        with get_db() as connection:
            return func(connection, *args, **kwargs)
    return wrapper

def perform_queries(connection: Connection, script_filename: str, query_separator=";"):
    script_file = path.join(database_directory, script_filename)
    with open(script_file, "r") as file_descriptor:
        queries = file_descriptor.read().split(query_separator)
        for query in queries:
            query = query.strip()
            connection.cursor().execute(query)
    connection.commit()


def setup_scheme(connection: Connection):
    perform_queries(connection, "setup_scheme.sql")


def populate_database(connection: Connection):
    perform_queries(connection, "populate_database.sql")
