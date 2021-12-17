from re import M
import sqlite3
from models import Seance
from db_config import with_database
from datetime import datetime
from dateutil import parser

import seance

@with_database
def get_all_seances(connection: sqlite3.Connection, params=None) -> list[Seance]:
    query = "SELECT seance.id, seance_datetime, cabinet, doctor_id, patient_id, diagnosis_id, procedure_id, doctor.surname, patient.surname, description, procedure_table.name FROM seance INNER JOIN doctor ON seance.doctor_id = doctor.id INNER JOIN patient ON seance.patient_id = patient.id INNER JOIN diagnosis ON seance.diagnosis_id = diagnosis.id INNER JOIN procedure_table ON seance.procedure_id = procedure_table.id"
    data = connection.cursor().execute(query).fetchall()
    seances = []
    
    for seance_tuple in data:
        
        seance_datatime = parser.parse(seance_tuple[1])
        seance = Seance(**{
            "id": seance_tuple[0],
            "seance_datatime": seance_datatime,
            "cabinet": seance_tuple[2],
            "doctor_id": seance_tuple[3],
            "patient_id": seance_tuple[4],
            "diagnosis_id": seance_tuple[5],
            "procedure_id": seance_tuple[6],
            "doctor": seance_tuple[7],
            "patient": seance_tuple[8],
            "diagnosis": seance_tuple[9],
            "procedure": seance_tuple[10]
        })
        seances.append(seance)
    return seances

@with_database
def remove_seance(connection: sqlite3.Connection, id_to_remove: int):
    query = f"DELETE FROM seance WHERE id={id_to_remove}"
    connection.cursor().execute(query)
    connection.commit()

@with_database
def add_seance(connection: sqlite3.Connection, seance: Seance):
    query = f'INSERT INTO seance(seance_datetime, cabinet, doctor_id, patient_id, diagnosis_id, procedure_id) VALUES("{seance.seance_datatime}", "{seance.cabinet}", "{seance.doctor_id}", "{seance.patient_id}", "{seance.diagnosis_id}", "{seance.procedure_id}")'
    connection.cursor().execute(query)
    connection.commit()

@with_database
def get_seance(connection: sqlite3.Connection, id: int) -> Seance:
    query = f"SELECT seance.id, seance_datetime, cabinet, doctor_id, patient_id, diagnosis_id, procedure_id, doctor.surname, patient.surname, description, procedure_table.name FROM seance INNER JOIN doctor ON seance.doctor_id = doctor.id INNER JOIN patient ON seance.patient_id = patient.id INNER JOIN diagnosis ON seance.diagnosis_id = diagnosis.id INNER JOIN procedure_table ON seance.procedure_id = procedure_table.id WHERE seance.id={id}"
    seance_array = connection.cursor().execute(query).fetchall()
    if not seance_array:
        return None
    seance_tuple = seance_array[0]
    seance_datetime = parser.parse(seance_tuple[1])
    return Seance(**{
            "id": seance_tuple[0],
            "seance_datatime": seance_datetime,
            "cabinet": seance_tuple[2],
            "doctor_id": seance_tuple[3],
            "patient_id": seance_tuple[4],
            "diagnosis_id": seance_tuple[5],
            "procedure_id": seance_tuple[6],
            "doctor": seance_tuple[7],
            "patient": seance_tuple[8],
            "diagnosis": seance_tuple[9],
            "procedure": seance_tuple[10]
    })


@with_database
def update_seance(connection: sqlite3.Connection, seance: Seance):
    
    query = f'UPDATE seance SET doctor_id={seance.doctor_id}, patient_id={seance.patient_id}, diagnosis_id={seance.diagnosis_id}, procedure_id={seance.procedure_id}, seance_datetime="{seance.seance_datatime}", cabinet={seance.cabinet} WHERE id={seance.id}'
    connection.cursor().execute(query)