from db_config import with_database
import sqlite3
from models import Clinic, Doctor

@with_database
def get_clinics_with_doctors(connection: sqlite3.Connection) -> list[Clinic]:
    data = connection.cursor().execute('SELECT * from clinic WHERE id IN(SELECT clinic_id from doctor);').fetchall()
    clinics = []
    for clinic_data in data:
        clinic = Clinic(**{
            'id': clinic_data[0],
            'address': clinic_data[1],
            'speciality': clinic_data[2],
            'clinic_type': clinic_data[3],
        })
        clinics.append(clinic)
    return clinics

@with_database
def get_doctors_of_patient(connection: sqlite3.Connection, patient_id: int) -> list[Doctor]:
    query = f'SELECT * FROM doctor INNER JOIN clinic ON doctor.clinic_id = clinic.id WHERE doctor.id = (SELECT doctor_id from seance WHERE seance.patient_id = {patient_id})'
    doctors_data = connection.cursor().execute(query).fetchall()
    result: list[Doctor] = []
    for doctor_data in doctors_data:
        result.append(Doctor(**{
             "id": doctor_data[0],
            "clinic_id": doctor_data[1],
            "name": doctor_data[2],
            "surname": doctor_data[3],
            "patronymic": doctor_data[4],
            "speciality": doctor_data[5],
            "address": doctor_data[7]
        }))
    return result
