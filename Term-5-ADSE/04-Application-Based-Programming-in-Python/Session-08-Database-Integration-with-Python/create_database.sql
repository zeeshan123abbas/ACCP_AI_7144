-- create_database.sql - run inside the MySQL command-line client
-- Open the client:  mysql -u root -p
-- Then run:        SOURCE create_database.sql;

-- 1) Create a database (a container for tables) and select it
CREATE DATABASE IF NOT EXISTS college;
USE college;

-- 2) Create a table with a primary key that numbers itself
CREATE TABLE IF NOT EXISTS students (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    name    VARCHAR(50)  NOT NULL,
    course  VARCHAR(30)  NOT NULL,
    marks   INT          DEFAULT 0
);

-- 3) Add a few sample rows
INSERT INTO students (name, course, marks) VALUES
    ('Ayesha', 'Python', 88),
    ('Bilal',  'Flutter', 67),
    ('Hamza',  'Python', 92);

-- 4) Check the data
SHOW TABLES;
DESCRIBE students;
SELECT * FROM students;

-- 5) A separate user for our Python app (better than using root)
CREATE USER IF NOT EXISTS 'student_app'@'localhost' IDENTIFIED BY 'Pass@1234';
GRANT ALL PRIVILEGES ON college.* TO 'student_app'@'localhost';
