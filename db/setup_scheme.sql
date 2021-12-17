 CREATE TABLE IF NOT EXISTS clinic (
	id INTEGER PRIMARY KEY,
  	address VARCHAR(32),
  	speciality VARCHAR(32),
  	type VARCHAR(32)
);


CREATE TABLE  IF NOT EXISTS doctor(
  	id INTEGER PRIMARY key,
    clinic_id INTEGER,
    name VARCHAR(32),
    surname VARCHAR(32),
    patronymic VARCHAR(32),
    speciality VARCHAR(32), 
    FOREIGN KEY (clinic_id) REFERENCES  clinic(id)
);

CREATE TABLE  IF NOT EXISTS patient(
  	id INTEGER PRIMARY key,
    name VARCHAR(32),
    surname VARCHAR(32),
    patronymic VARCHAR(32),
    address VARCHAR(32), 
	birth DATE
);

CREATE TABLE  IF NOT EXISTS procedure_table(
	id INTEGER PRIMARY KEY,
	name VARCHAR(32),
	duration INTEGER,
	price INTEGER
);

CREATE TABLE  IF NOT EXISTS diagnosis(
	id INTEGER PRIMARY KEY,
	description VARCHAR(32)
);

CREATE TABLE  IF NOT EXISTS seance(
	id INTEGER PRIMARY KEY,
	seance_datetime DATETIME,
	cabinet INTEGER,
	doctor_id INTEGER,
	patient_id INTEGER,
	diagnosis_id INTEGER,
	procedure_id INTEGER,
	FOREIGN KEY (doctor_id) REFERENCES doctor(id),
	FOREIGN KEY (patient_id) REFERENCES patient(id),
	FOREIGN KEY (diagnosis_id) REFERENCES diagnosis(id),
	FOREIGN KEY (procedure_id) REFERENCES procedure_table(id)
);