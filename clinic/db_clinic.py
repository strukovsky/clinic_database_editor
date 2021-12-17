from sqlite3 import Connection
from db_config import with_database
from models import Clinic

@with_database
def get_all_clinics(connection: Connection=None) -> list[Clinic]:
    cursor = connection.cursor().execute("SELECT * FROM clinic")
    clinics_data = cursor.fetchall()
    clinics = []
    for clinic_data_tuple in clinics_data:
        clinic_id = clinic_data_tuple[0]
        address = clinic_data_tuple[1]
        speciality = clinic_data_tuple[2]
        clinic_type = clinic_data_tuple[3]
        clinic_data = {
            "id": clinic_id,
            "address": address,
             "speciality": speciality,
             "clinic_type": clinic_type
        }
        clinic = Clinic(**clinic_data)
        clinics.append(clinic)
    return clinics

@with_database
def add_clinic(connection: Connection, params: Clinic):
    clinic = params
    address = clinic.address
    speciality = clinic.speciality
    clinic_type = clinic.clinic_type
    query = f"INSERT OR IGNORE INTO clinic(address, speciality, type) VALUES('{address}', '{speciality}', '{clinic_type}')"
    connection.cursor().execute(query)
    connection.commit()
        
@with_database
def get_clinic(connection: Connection, id: int) -> Clinic:
    query = f"SELECT * FROM clinic WHERE id={id}"
    cursor = connection.cursor().execute(query)
    clinic_data_tuple = cursor.fetchall()[0]
    clinic_data = {
        "id": clinic_data_tuple[0],
        "address": clinic_data_tuple[1],
        "speciality": clinic_data_tuple[2],
        "clinic_type": clinic_data_tuple[3],
    }        
    return Clinic(**clinic_data)


@with_database
def update_clinic(connection: Connection, clinic: Clinic):
    query = f"UPDATE clinic SET address=\"{clinic.address}\", speciality=\"{clinic.speciality}\", type=\"{clinic.clinic_type}\" WHERE id={clinic.id}"
    connection.cursor().execute(query)

@with_database
def remove_clinic(connection: Connection, id_to_remove: int):
    query = f"DELETE FROM clinic WHERE id={id_to_remove}"
    connection.cursor().execute(query)
    connection.commit()