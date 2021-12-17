import sqlite3
from db_config import with_database
from models import Patient
from dateutil import parser

@with_database
def get_all_patients(connection: sqlite3.Connection) -> list[Patient]:
    query = "SELECT * FROM patient"
    patients_data = connection.cursor().execute(query).fetchall()
    patients = []
    for patient_data  in patients_data:
        date_string = str(patient_data[5])
        date_object = parser.parse(date_string)
        patients.append(Patient(**{
            "id": patient_data[0],
            "name": patient_data[1],
            "surname": patient_data[2],
            "patronymic": patient_data[3],
            "address": patient_data[4],
            "birth": date_object
        }))
    return patients


@with_database
def add_patient(connection: sqlite3.Connection, patient: Patient) -> str:
    query = f'INSERT INTO patient(id, name, surname, patronymic, address, birth) VALUES({patient.id}, "{patient.name}", "{patient.surname}", "{patient.patronymic}", "{patient.address}", "{patient.birth}")'
    try: 
        connection.cursor().execute(query)
        connection.commit()
    except Exception as e:
        return "already_exists"
    return "OK"


@with_database
def remove_patient(connection: sqlite3.Connection, id_to_remove: int):
    query = f"DELETE FROM patient WHERE id={id_to_remove}"
    connection.cursor().execute(query)
    connection.commit()

@with_database
def get_patient(connection: sqlite3.Connection, patient_id: int):
    query = f"SELECT * FROM patient WHERE id={patient_id}"
    data = connection.cursor().execute(query).fetchone()
    return Patient(**{
        "id": data[0],
        "name": data[1],
        "surname": data[2],
        "patronymic": data[3],
        "address": data[4],
        "birth": parser.parse(data[5])
    })


@with_database
def edit_patient(connection: sqlite3.Connection, patient: Patient):
    query = f'UPDATE patient SET surname="{patient.surname}", name="{patient.name}", patronymic="{patient.patronymic}", address="{patient.address}", birth="{patient.birth}" WHERE id={patient.id}'
    connection.cursor().execute(query)