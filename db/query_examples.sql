
-- Task 1. Each select, delete or update query should be sent to sqliteonline.com one by one, query by query.
SELECT speciality from clinic UNION SELECT speciality from doctor
SELECT doctor_id from seance UNION SELECT id from doctor
SELECT procedure_id from seance UNION SELECT id from procedure_table


-- Task 2
SELECT * from patient WHERE id = (SELECT patient_id from seance);
SELECT * from clinic WHERE id IN(SELECT clinic_id from doctor); -- IN is analog in SQLite of ANY in MS SQL
SELECT * FROM doctor where doctor.id = (SELECT doctor_id from seance WHERE seance.patient_id = 2);
SELECT EXISTS (SELECT * from clinic WHERE clinic.id = (SELECT clinic_id from doctor WHERE doctor.id = 1));
SELECT * from patient, seance WHERE seance.patient_id = patient.id GROUP BY patient.surname, patient.name HAVING
COUNT(seance.id) >= (SELECT MAX(seance.id) FROM seance WHERE seance.patient_id = patient.id); -- MAX is used due to lack of ALL in SQLite

-- Task 3
INSERT INTO doctor (clinic_id, speciality) SELECT clinic_id, speciality FROM doctor WHERE clinic_id = 1;
INSERT INTO clinic(speciality) SELECT speciality FROM clinic WHERE clinic.id = 1;
INSERT INTO diagnosis (description) SELECT description from diagnosis WHERE id = (SELECT diagnosis_id FROM seance WHERE patient_id = 1);

-- Task 4
UPDATE doctor SET speciality = 'Specialist' WHERE 1 < (SELECT COUNT(*) FROM seance WHERE seance.doctor_id = doctor.id);
UPDATE patient SET surname = 'Strukovsky' WHERE id = 1;
UPDATE procedure_table SET price = 1000 WHERE id = 2;
UPDATE diagnosis SET description = 'Bolyachka' WHERE id = 3;
UPDATE clinic SET speciality = 'Stomache' WHERE id = 2;

-- Task 5
DELETE FROM clinic WHERE speciality = 'Stomache';
DELETE FROM procedure_table WHERE id in (SELECT procedure_id from seance WHERE patient_id = 1);
DELETE FROM diagnosis WHERE id = 2;




































