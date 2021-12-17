from re import M
import sqlite3
from models import Diagnosis
from db_config import with_database


@with_database
def get_all_diagnosiss(connection: sqlite3.Connection, params=None) -> list[Diagnosis]:
    query = "SELECT * FROM diagnosis"
    data = connection.cursor().execute(query).fetchall()
    diagnosiss = []
    for diagnosis_tuple in data:
        diagnosis = Diagnosis(**{
            "id": diagnosis_tuple[0],    
            "description": diagnosis_tuple[1],
        })
        diagnosiss.append(diagnosis)
    return diagnosiss

@with_database
def remove_diagnosis(connection: sqlite3.Connection, id_to_remove: int):
    query = f"DELETE FROM diagnosis WHERE id={id_to_remove}"
    connection.cursor().execute(query)
    connection.commit()

@with_database
def add_diagnosis(connection: sqlite3.Connection, diagnosis: Diagnosis):
    query = f'INSERT INTO diagnosis(description) VALUES("{diagnosis.description}")'
    connection.cursor().execute(query)
    connection.commit()

@with_database
def get_diagnosis(connection: sqlite3.Connection, id: int) -> Diagnosis:
    query = f"SELECT * FROM diagnosis WHERE diagnosis.id={id}"
    data = connection.cursor().execute(query).fetchall()[0]
    return Diagnosis(**{
        "id": data[0],
        "description": data[1]
    })


@with_database
def update_diagnosis(connection: sqlite3.Connection, diagnosis: Diagnosis):
    query = f'UPDATE diagnosis SET description="{diagnosis.description}" WHERE id={diagnosis.id}'
    connection.cursor().execute(query)