-- functions.sql
USE institute_db;

SELECT UPPER(full_name)                         AS name_caps,
       CONCAT(LEFT(full_name, 1), '.', city)    AS short_tag,
       CHAR_LENGTH(full_name)                   AS name_length,
       TIMESTAMPDIFF(YEAR, dob, CURDATE())      AS age,
       DATE_FORMAT(created_at, '%d-%b-%Y')      AS joined,
       IFNULL(dob, 'not given')                 AS dob_or_text
FROM students;

SELECT title, fee, ROUND(fee / weeks) AS fee_per_week,
       CASE WHEN fee >= 30000 THEN 'Premium'
            WHEN fee >= 20000 THEN 'Standard'
            ELSE 'Short course' END AS band
FROM courses;

SELECT c.title, GROUP_CONCAT(s.full_name ORDER BY s.full_name SEPARATOR ', ') AS students
FROM courses c
JOIN enrollments e ON e.course_id = c.course_id
JOIN students s ON s.student_id = e.student_id
GROUP BY c.title;
