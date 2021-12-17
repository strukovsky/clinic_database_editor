from re import M
import sqlite3
from models import Doctor
from db_config import with_database


@with_database
def get_all_doctors(connection: sqlite3.Connection, params=None) -> list[Doctor]:
    query = "SELECT * FROM doctor INNER JOIN clinic ON doctor.clinic_id = clinic.id"
    data = connection.cursor().execute(query).fetchall()
    doctors = []
    for doctor_tuple in data:
        clinic_id = doctor_tuple[1]
        clinic_address = doctor_tuple[7]
        doctor = Doctor(**{
            "id": doctor_tuple[0],
            "clinic_id": clinic_id,
            "name": doctor_tuple[2],
            "surname": doctor_tuple[3],
            "patronymic": doctor_tuple[4],
            "speciality": doctor_tuple[5],
            "address": clinic_address
        })
        doctors.append(doctor)
    return doctors

@with_database
def remove_doctor(connection: sqlite3.Connection, id_to_remove: int):
    query = f"DELETE FROM doctor WHERE id={id_to_remove}"
    connection.cursor().execute(query)
    connection.commit()

@with_database
def add_doctor(connection: sqlite3.Connection, doctor: Doctor):
    query = f'INSERT INTO doctor(clinic_id, name, surname, patronymic, speciality) VALUES({doctor.clinic_id}, "{doctor.name}", "{doctor.surname}", "{doctor.patronymic}", "{doctor.speciality}")'
    connection.cursor().execute(query)
    connection.commit()

@with_database
def get_doctor(connection: sqlite3.Connection, id: int) -> Doctor:
    query = f"SELECT doctor.id, clinic_id, name, surname, patronymic, doctor.speciality, address FROM doctor INNER JOIN clinic ON doctor.clinic_id = clinic.id WHERE doctor.id={id}"
    data = connection.cursor().execute(query).fetchall()[0]
    return Doctor(**{
        "id": data[0],
        "clinic_id": data[1],
        "name": data[2],
        "surname": data[3],
        "patronymic": data[4],
        "speciality": data[5],
        "address": data[6]
    })


@with_database
def update_doctor(connection: sqlite3.Connection, doctor: Doctor):
    query = f'UPDATE doctor SET clinic_id={doctor.clinic_id}, name="{doctor.name}", surname="{doctor.surname}", patronymic="{doctor.patronymic}", speciality="{doctor.speciality}" WHERE id={doctor.id}'
    connection.cursor().execute(query)