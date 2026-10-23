-- normalization-walkthrough.sql
CREATE DATABASE IF NOT EXISTS design_demo;
USE design_demo;

-- UNNORMALIZED: multiple values in one cell (violates 1NF)
CREATE TABLE raw_enrollments (
  student_id INT,
  student_name VARCHAR(100),
  courses VARCHAR(255),          -- 'PHP:Mr. Imran:0300-1111111, MySQL:Ms. Hina:0301-2222222'
  city VARCHAR(50)
);

-- 1NF: one value per cell, composite PK
CREATE TABLE enrollments_1nf (
  student_id INT,
  student_name VARCHAR(100),
  city VARCHAR(50),
  course_code VARCHAR(10),
  course_title VARCHAR(100),
  faculty_name VARCHAR(100),
  faculty_phone VARCHAR(20),
  PRIMARY KEY (student_id, course_code)
);
-- Problem: student_name and city depend only on student_id (partial dependency)

-- 2NF: split out data that depends on part of the key
CREATE TABLE students_2nf (
  student_id INT PRIMARY KEY,
  student_name VARCHAR(100),
  city VARCHAR(50)
);
CREATE TABLE courses_2nf (
  course_code VARCHAR(10) PRIMARY KEY,
  course_title VARCHAR(100),
  faculty_name VARCHAR(100),
  faculty_phone VARCHAR(20)      -- depends on faculty_name, not course_code (transitive)
);
CREATE TABLE enrollments_2nf (
  student_id INT,
  course_code VARCHAR(10),
  PRIMARY KEY (student_id, course_code)
);

-- 3NF: remove the transitive dependency course -> faculty -> phone
CREATE TABLE faculty (
  faculty_id INT AUTO_INCREMENT PRIMARY KEY,
  faculty_name VARCHAR(100) NOT NULL,
  phone VARCHAR(20) UNIQUE
);
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  student_name VARCHAR(100) NOT NULL,
  city VARCHAR(50)
);
CREATE TABLE courses (
  course_code VARCHAR(10) PRIMARY KEY,
  course_title VARCHAR(100) NOT NULL,
  faculty_id INT,
  FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);
CREATE TABLE enrollments (
  student_id INT,
  course_code VARCHAR(10),
  enrolled_on DATE DEFAULT (CURRENT_DATE),
  PRIMARY KEY (student_id, course_code),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_code) REFERENCES courses(course_code)
);
