-- first-queries.sql : run in MySQL Workbench or the mysql command-line client

-- 1. Server information
SELECT VERSION() AS mysql_version, CURRENT_USER() AS logged_in_as, NOW() AS server_time;

-- 2. Which databases exist?
SHOW DATABASES;

-- 3. Create and use a practice database
CREATE DATABASE IF NOT EXISTS institute_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE institute_db;

-- 4. A first table
CREATE TABLE IF NOT EXISTS students (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  full_name  VARCHAR(100) NOT NULL,
  city       VARCHAR(50)  DEFAULT 'Karachi',
  joined_on  DATE
);

-- 5. Insert and read data
INSERT INTO students (full_name, city, joined_on) VALUES
  ('Ayesha Khan', 'Karachi', '2025-01-15'),
  ('Bilal Ahmed', 'Hyderabad', '2025-02-01'),
  ('Sana Javed', DEFAULT, '2025-02-10');

SELECT * FROM students;

-- 6. Describe the structure
DESCRIBE students;
SHOW TABLES;
