from re import M
import sqlite3
from models import Doctor, Procedure
from db_config import with_database


@with_database
def get_all_procedures(connection: sqlite3.Connection, params=None) -> list[Procedure]:
    query = "SELECT * FROM procedure_table"
    data = connection.cursor().execute(query).fetchall()
    procedures = []
    for procedure_tuple in data:
        procedure = Procedure(**{
            "id": procedure_tuple[0],
            "name": procedure_tuple[1],
            "duration": procedure_tuple[2],
            "price": procedure_tuple[3],
        })
        procedures.append(procedure)
    return procedures

@with_database
def remove_procedure(connection: sqlite3.Connection, id_to_remove: int):
    query = f"DELETE FROM procedure_table WHERE id={id_to_remove}"
    connection.cursor().execute(query)
    connection.commit()

@with_database
def add_procedure(connection: sqlite3.Connection, procedure: Procedure):
    query = f'INSERT INTO procedure_table(name, duration, price) VALUES("{procedure.name}", "{procedure.duration}", "{procedure.price}")'
    connection.cursor().execute(query)
    connection.commit()

@with_database
def get_procedure(connection: sqlite3.Connection, id: int) -> Procedure:
    query = f"SELECT * FROM procedure_table WHERE id={id}"
    data = connection.cursor().execute(query).fetchall()[0]
    return Procedure(**{
        "id": data[0],
        "name": data[1],
        "duration": data[2],
        "price": data[3]
    })


@with_database
def update_procedure(connection: sqlite3.Connection, procedure: Doctor):
    query = f'UPDATE procedure_table SET name="{procedure.name}", price="{procedure.price}", duration="{procedure.duration}" WHERE id={procedure.id}'
    connection.cursor().execute(query)