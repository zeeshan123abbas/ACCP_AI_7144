-- select-practice.sql
USE institute_db;

-- 1. All columns, then chosen columns with aliases
SELECT * FROM courses;
SELECT code AS "Course Code", title, fee AS "Fee (PKR)" FROM courses;

-- 2. Calculated column
SELECT title, fee, ROUND(fee * 0.90) AS fee_after_10pct_discount FROM courses;

-- 3. WHERE with comparison and logical operators
SELECT full_name, city FROM students WHERE city = 'Karachi';
SELECT full_name, city, gender FROM students WHERE city = 'Karachi' AND gender = 'female';
SELECT title, fee, weeks FROM courses WHERE fee > 25000 AND (weeks >= 6 OR code = 'LRVL01');
SELECT full_name FROM students WHERE NOT city = 'Karachi';

-- 4. NULL handling
SELECT student_id, course_id FROM enrollments WHERE marks IS NULL;  -- results pending
SELECT title FROM courses WHERE faculty_id IS NULL;                 -- no teacher assigned

-- 5. Sorting
SELECT full_name, dob FROM students ORDER BY dob;                   -- oldest first
SELECT title, fee FROM courses ORDER BY fee DESC, title;

-- 6. Top-N and pagination
SELECT student_id, course_id, marks FROM enrollments
WHERE marks IS NOT NULL ORDER BY marks DESC LIMIT 3;                -- top 3 marks

SELECT student_id, full_name FROM students ORDER BY student_id LIMIT 4 OFFSET 4;  -- page 2 (size 4)

-- 7. Insert a student, then use the generated id
INSERT INTO students (full_name, email, gender, city) VALUES ('Rida Fatima', 'rida@mail.com', 'female', 'Multan');
SELECT LAST_INSERT_ID() AS new_student_id;

-- 8. INSERT ... SELECT : copy Karachi students into a new table
CREATE TABLE IF NOT EXISTS karachi_students LIKE students;
INSERT INTO karachi_students SELECT * FROM students WHERE city = 'Karachi';
SELECT COUNT(*) AS copied FROM karachi_students;
