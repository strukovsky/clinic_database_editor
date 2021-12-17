from pydantic import BaseModel
from datetime import date, datetime

class Clinic(BaseModel):
    id: int
    address: str
    speciality: str
    clinic_type: str


class Doctor(BaseModel):
    id: int
    clinic_id: int
    name: str
    surname: str
    patronymic: str
    speciality: str
    address: str

class Patient(BaseModel):
    id: int
    name: str
    surname: str
    patronymic: str
    address: str
    birth: date

class Procedure(BaseModel):
    id: int
    name: str
    duration: int
    price: int

class Diagnosis(BaseModel):
    id: int
    description: str

class Seance(BaseModel):
    id: int
    seance_datatime: datetime
    cabinet: int
    doctor_id: int
    patient_id: int
    diagnosis_id: int
    procedure_id: int
    doctor: str
    patient: str
    diagnosis: str
    procedure: str