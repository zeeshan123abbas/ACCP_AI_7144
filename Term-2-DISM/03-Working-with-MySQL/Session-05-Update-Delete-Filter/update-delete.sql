-- update-delete.sql  (uses institute_db with seed data)
USE institute_db;

-- Workbench Safe Updates blocks UPDATE/DELETE whose WHERE does not use a key column.
-- For this practice script only, switch it off for the session and back on at the end.
SET SQL_SAFE_UPDATES = 0;

-- 1. Preview, then update one row
SELECT student_id, full_name, city FROM students WHERE email = 'zoya@mail.com';
UPDATE students SET city = 'Karachi', dob = '2004-06-06' WHERE email = 'zoya@mail.com';

-- 2. Expression update: increase all course fees above 25,000 by 5%
SELECT code, fee, ROUND(fee * 1.05, 2) AS new_fee FROM courses WHERE fee > 25000;  -- preview
UPDATE courses SET fee = ROUND(fee * 1.05, 2) WHERE fee > 25000;

-- 3. Conditional update with CASE: give grace marks to scores 45-49
UPDATE enrollments
SET marks = CASE WHEN marks BETWEEN 45 AND 49 THEN 50 ELSE marks END
WHERE marks IS NOT NULL AND marks < 50;

-- 4. Soft delete: add a flag and deactivate instead of deleting
ALTER TABLE students ADD COLUMN is_active TINYINT(1) NOT NULL DEFAULT 1;
UPDATE students SET is_active = 0 WHERE student_id = 9;
SELECT full_name FROM students WHERE is_active = 1;

-- 5. Hard delete: remove a payment recorded by mistake
SELECT * FROM payments WHERE payment_id = 16;
DELETE FROM payments WHERE payment_id = 16;

-- 6. Delete blocked by a foreign key (RESTRICT): try it and read the error
-- DELETE FROM courses WHERE course_id = 1;   -- Error 1451: cannot delete a parent row

SET SQL_SAFE_UPDATES = 1;
