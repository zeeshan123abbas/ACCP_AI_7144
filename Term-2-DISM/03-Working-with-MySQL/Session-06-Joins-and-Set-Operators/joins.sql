-- joins.sql
USE institute_db;

-- 1. INNER JOIN: result card (student, course, marks)
SELECT s.full_name, c.title, e.marks
FROM students s
INNER JOIN enrollments e ON e.student_id = s.student_id
INNER JOIN courses c     ON c.course_id  = e.course_id
ORDER BY s.full_name, c.title;

-- 2. Four tables: who teaches each enrolled student
SELECT s.full_name AS student, c.title AS course, f.full_name AS teacher
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses  c ON c.course_id  = e.course_id
LEFT JOIN faculty f ON f.faculty_id = c.faculty_id;   -- LEFT: CMS course has no teacher

-- 3. LEFT JOIN: all students, enrolled or not
SELECT s.full_name, e.course_id
FROM students s
LEFT JOIN enrollments e ON e.student_id = s.student_id
ORDER BY s.full_name;

-- 4. Anti-join: students with NO enrollments
SELECT s.full_name
FROM students s
LEFT JOIN enrollments e ON e.student_id = s.student_id
WHERE e.enrollment_id IS NULL;

-- 5. RIGHT JOIN: every course, even with no enrollments
SELECT c.title, e.student_id
FROM enrollments e
RIGHT JOIN courses c ON c.course_id = e.course_id
ORDER BY c.title;

-- 6. FULL OUTER JOIN emulation: courses vs faculty
SELECT c.title, f.full_name FROM courses c LEFT JOIN faculty f ON f.faculty_id = c.faculty_id
UNION
SELECT c.title, f.full_name FROM courses c RIGHT JOIN faculty f ON f.faculty_id = c.faculty_id;

-- 7. Condition in ON vs WHERE
SELECT s.full_name, e.marks
FROM students s
LEFT JOIN enrollments e ON e.student_id = s.student_id AND e.marks >= 90;  -- keeps all students

-- 8. SELF JOIN: pairs of students from the same city
SELECT a.full_name AS student_1, b.full_name AS student_2, a.city
FROM students a
JOIN students b ON a.city = b.city AND a.student_id < b.student_id
ORDER BY a.city;

-- 9. CROSS JOIN: every faculty × course combination (planning grid)
SELECT f.full_name, c.code FROM faculty f CROSS JOIN courses c LIMIT 10;
