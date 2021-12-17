INSERT or IGNORE INTO clinic VALUES(1, 'Yunosti Street', 'Therapy', 'Clinic');
INSERT or IGNORE  INTO clinic VALUES(2, 'Nikolaeva Street', 'Balneologic', 'Hospital');
INSERT or IGNORE  INTO clinic VALUES(3, 'Semenovskaya Street', 'Psychotherapy', 'Clinic');

INSERT or IGNORE INTO doctor VALUES(1, 1, 'Samples', 'Yaroslav', 'Petrovich', 'Psychologist');
INSERT or IGNORE INTO doctor VALUES(2, 2, 'Nikolaev', 'Alexey', 'Victorovich', 'Nursery');
INSERT or IGNORE INTO doctor VALUES(3, 2, 'Semenov', 'Dmitrii', 'Dmitrievich', 'Surgery');
INSERT or IGNORE INTO doctor VALUES(4, 3, 'Torgov', 'Alexander', 'Dmitrievich', 'Surgery');
INSERT or IGNORE INTO doctor VALUES(5, 3, 'Victorov', 'Maxim', 'Sample', 'Psychologist');

INSERT or IGNORE INTO procedure_table VALUES(1, 'Psychotherapy', 60, 1000);
INSERT or IGNORE INTO procedure_table VALUES(2, 'Surgery', 360, 10000);
INSERT or IGNORE INTO procedure_table VALUES(3, 'Preparation', 20, 500);


INSERT or IGNORE INTO diagnosis VALUES(1, 'Illness');
INSERT or IGNORE INTO diagnosis VALUES(2, 'Fatigue');
INSERT or IGNORE INTO diagnosis VALUES(3, 'Stomachache');

INSERT or IGNORE INTO patient VALUES(1, 'Nikolaev', 'Dmitry', 'Semnovich', 'Yunosti 15', '11.10.2004');
INSERT or IGNORE INTO patient VALUES(2, 'Victorov', 'Semen', 'Genadievich', 'Yunosti 11', '01.05.2000');
INSERT or IGNORE INTO patient VALUES(3, 'Morozov', 'Yury', 'Nikolaevich', 'Yunosti 7', '03.15.2010');

INSERT OR IGNORE INTO seance VALUES(1, '03.10.2020 11:10:35', 210, 2, 3, 3, 1);
INSERT OR IGNORE INTO seance VALUES(2, '05.10.2020 12:10:35', 240, 3, 2, 1, 1);
INSERT OR IGNORE INTO seance VALUES(3, '10.11.2020 15:10:36', 310, 1, 2, 3, 2);