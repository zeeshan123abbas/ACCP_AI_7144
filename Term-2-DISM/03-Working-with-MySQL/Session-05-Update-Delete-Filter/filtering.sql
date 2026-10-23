-- filtering.sql
USE institute_db;

-- LIKE patterns
SELECT full_name FROM students WHERE full_name LIKE 'A%';        -- starts with A
SELECT full_name FROM students WHERE full_name LIKE '%a';        -- ends with a
SELECT full_name FROM students WHERE full_name LIKE '%ra%';      -- contains "ra"
SELECT full_name FROM students WHERE full_name LIKE '_a%';       -- second letter a
SELECT email FROM students WHERE email NOT LIKE '%@mail.com';

-- BETWEEN (inclusive) with numbers and dates
SELECT title, fee FROM courses WHERE fee BETWEEN 20000 AND 30000;
SELECT full_name, dob FROM students WHERE dob BETWEEN '2004-01-01' AND '2004-12-31';
SELECT payment_id, paid_on FROM payments WHERE paid_on BETWEEN '2025-03-01' AND '2025-03-31 23:59:59';

-- IN / NOT IN
SELECT full_name, city FROM students WHERE city IN ('Lahore', 'Islamabad', 'Sukkur');
SELECT code, title FROM courses WHERE code NOT IN ('XMLJ01', 'CMSW01');

-- REGEXP
SELECT full_name FROM students WHERE full_name REGEXP '^[AEIOU]';

-- DISTINCT
SELECT DISTINCT city FROM students ORDER BY city;
SELECT DISTINCT method FROM payments;
SELECT COUNT(DISTINCT city) AS number_of_cities FROM students;

-- Upsert 1: ON DUPLICATE KEY UPDATE (email is UNIQUE)
INSERT INTO students (full_name, email, gender, city)
VALUES ('Ayesha Khan', 'ayesha@mail.com', 'female', 'Hyderabad')
ON DUPLICATE KEY UPDATE city = VALUES(city);   -- updates Ayesha's city instead of failing

-- Upsert 2: INSERT IGNORE skips the duplicate silently (check SHOW WARNINGS)
INSERT IGNORE INTO students (full_name, email, gender) VALUES ('Duplicate', 'bilal@mail.com', 'male');
SHOW WARNINGS;

-- Upsert 3: REPLACE deletes then inserts (new row, cascades fire!) — demo on a safe table
CREATE TABLE IF NOT EXISTS settings (setting_key VARCHAR(50) PRIMARY KEY, setting_value VARCHAR(100));
REPLACE INTO settings VALUES ('theme', 'light');
REPLACE INTO settings VALUES ('theme', 'dark');
SELECT * FROM settings;
