-- institute-schema.sql : the database used in the rest of this module
DROP DATABASE IF EXISTS institute_db;
CREATE DATABASE institute_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE institute_db;

CREATE TABLE faculty (
  faculty_id  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name   VARCHAR(100) NOT NULL,
  email       VARCHAR(120) NOT NULL UNIQUE,
  salary      DECIMAL(10,2) CHECK (salary > 0),
  hired_on    DATE NOT NULL
);

CREATE TABLE students (
  student_id  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name   VARCHAR(100) NOT NULL,
  email       VARCHAR(120) NOT NULL UNIQUE,
  gender      ENUM('male','female','other') NOT NULL,
  dob         DATE,
  city        VARCHAR(50) NOT NULL DEFAULT 'Karachi',
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courses (
  course_id   INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  code        CHAR(6) NOT NULL UNIQUE,
  title       VARCHAR(100) NOT NULL,
  weeks       TINYINT UNSIGNED NOT NULL CHECK (weeks BETWEEN 1 AND 52),
  fee         DECIMAL(9,2) NOT NULL CHECK (fee >= 0),
  faculty_id  INT UNSIGNED,
  CONSTRAINT fk_course_faculty FOREIGN KEY (faculty_id)
    REFERENCES faculty(faculty_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE enrollments (
  enrollment_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  student_id    INT UNSIGNED NOT NULL,
  course_id     INT UNSIGNED NOT NULL,
  enrolled_on   DATE NOT NULL DEFAULT (CURRENT_DATE),
  marks         TINYINT UNSIGNED CHECK (marks <= 100),
  CONSTRAINT uq_student_course UNIQUE (student_id, course_id),
  CONSTRAINT fk_enr_student FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  CONSTRAINT fk_enr_course  FOREIGN KEY (course_id)  REFERENCES courses(course_id)  ON DELETE RESTRICT
);

CREATE TABLE payments (
  payment_id    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  enrollment_id INT UNSIGNED NOT NULL,
  amount        DECIMAL(9,2) NOT NULL CHECK (amount > 0),
  paid_on       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  method        ENUM('cash','card','bank') NOT NULL,
  FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE
);

SHOW TABLES;
SHOW CREATE TABLE enrollments;
