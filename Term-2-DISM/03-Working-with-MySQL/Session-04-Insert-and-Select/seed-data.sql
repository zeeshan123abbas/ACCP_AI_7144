-- seed-data.sql : run after Session 03's institute-schema.sql
USE institute_db;

INSERT INTO faculty (full_name, email, salary, hired_on) VALUES
  ('Imran Javed',   'imran@inst.pk', 185000, '2019-06-01'),
  ('Hina Rauf',     'hina@inst.pk',  165000, '2021-02-15'),
  ('Kashif Mehmood','kashif@inst.pk',210000, '2016-09-10'),
  ('Sadia Noor',    'sadia@inst.pk', 120000, '2024-01-08');

INSERT INTO students (full_name, email, gender, dob, city) VALUES
  ('Ayesha Khan',   'ayesha@mail.com', 'female', '2004-05-12', 'Karachi'),
  ('Bilal Ahmed',   'bilal@mail.com',  'male',   '2003-11-02', 'Hyderabad'),
  ('Sana Javed',    'sana@mail.com',   'female', '2005-01-25', 'Karachi'),
  ('Usman Ali',     'usman@mail.com',  'male',   '2002-07-30', 'Lahore'),
  ('Fatima Zahra',  'fatima@mail.com', 'female', '2004-09-18', 'Karachi'),
  ('Hamza Siddiqui','hamza@mail.com',  'male',   '2005-03-03', 'Sukkur'),
  ('Mariam Iqbal',  'mariam@mail.com', 'female', '2003-12-21', 'Islamabad'),
  ('Danish Raza',   'danish@mail.com', 'male',   '2004-02-14', 'Karachi'),
  ('Zoya Baig',     'zoya@mail.com',   'female', NULL,         'Lahore'),
  ('Ahmed Shah',    'ahmed@mail.com',  'male',   '2001-08-08', 'Karachi');

INSERT INTO courses (code, title, weeks, fee, faculty_id) VALUES
  ('XMLJ01', 'Data Processing with XML and JSON', 3, 15000, 2),
  ('JSPR01', 'Programming with JavaScript',       6, 28000, 1),
  ('MYSQ01', 'Working with MySQL',                6, 26000, 3),
  ('PHPW01', 'Dynamic Web Development with PHP',  9, 42000, 1),
  ('LRVL01', 'Laravel Framework',                 4, 30000, 3),
  ('CMSW01', 'Websites with CMS',                 4, 22000, NULL);

INSERT INTO enrollments (student_id, course_id, enrolled_on, marks) VALUES
  (1,1,'2025-01-20',88),(1,2,'2025-02-15',91),(1,3,'2025-03-20',79),
  (2,1,'2025-01-20',64),(2,3,'2025-03-20',72),
  (3,2,'2025-02-15',55),(3,4,'2025-05-01',NULL),
  (4,3,'2025-03-20',95),(4,4,'2025-05-01',87),(4,5,'2025-08-01',90),
  (5,1,'2025-01-20',47),(5,2,'2025-02-15',68),
  (6,4,'2025-05-01',NULL),
  (7,2,'2025-02-15',82),(7,3,'2025-03-20',77),(7,5,'2025-08-01',NULL),
  (8,1,'2025-01-20',73),
  (10,3,'2025-03-20',38);

INSERT INTO payments (enrollment_id, amount, paid_on, method) VALUES
  (1,15000,'2025-01-20 10:00','cash'),(2,28000,'2025-02-15 11:30','card'),
  (3,13000,'2025-03-20 09:15','bank'),(3,13000,'2025-04-20 09:20','bank'),
  (4,15000,'2025-01-21 12:00','cash'),(5,26000,'2025-03-22 16:45','card'),
  (6,14000,'2025-02-16 10:10','cash'),(8,26000,'2025-03-20 13:00','bank'),
  (9,21000,'2025-05-02 15:00','card'),(9,21000,'2025-06-02 15:05','card'),
  (10,30000,'2025-08-01 10:30','bank'),(11,15000,'2025-01-20 14:00','cash'),
  (14,28000,'2025-02-17 11:00','card'),(15,26000,'2025-03-21 12:00','bank'),
  (17,15000,'2025-01-22 09:00','cash'),(18,10000,'2025-03-25 17:30','cash');
