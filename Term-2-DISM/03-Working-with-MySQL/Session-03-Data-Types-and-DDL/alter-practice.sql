-- alter-practice.sql  (run after institute-schema.sql)
USE institute_db;

-- Add columns
ALTER TABLE students
  ADD COLUMN phone VARCHAR(15) AFTER email,
  ADD COLUMN cnic CHAR(15) UNIQUE;

-- Modify a column type/size and nullability
ALTER TABLE students MODIFY COLUMN phone VARCHAR(20) NOT NULL DEFAULT '';

-- Rename a column
ALTER TABLE students RENAME COLUMN phone TO mobile;

-- Add a CHECK constraint with a name
ALTER TABLE students ADD CONSTRAINT chk_dob CHECK (dob > '1950-01-01');

-- Remove a column
ALTER TABLE students DROP COLUMN cnic;

-- Inspect the result
DESCRIBE students;

-- Temporary table for experiments: TRUNCATE vs DROP
CREATE TABLE temp_logs (id INT AUTO_INCREMENT PRIMARY KEY, msg VARCHAR(100));
INSERT INTO temp_logs (msg) VALUES ('a'), ('b'), ('c');
TRUNCATE TABLE temp_logs;              -- rows gone, AUTO_INCREMENT reset
INSERT INTO temp_logs (msg) VALUES ('new');
SELECT * FROM temp_logs;               -- id is 1 again
DROP TABLE IF EXISTS temp_logs;        -- table gone completely
