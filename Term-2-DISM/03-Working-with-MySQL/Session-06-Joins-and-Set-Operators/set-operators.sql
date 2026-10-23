-- set-operators.sql
USE institute_db;

-- UNION: one contact list of everyone at the institute (duplicates removed)
SELECT full_name, email, 'student' AS role FROM students
UNION
SELECT full_name, email, 'faculty' FROM faculty
ORDER BY role, full_name;

-- UNION ALL keeps duplicates: courses joined by student 1 and student 4
SELECT course_id FROM enrollments WHERE student_id = 1
UNION ALL
SELECT course_id FROM enrollments WHERE student_id = 4;

-- INTERSECT (MySQL 8.0.31+): courses taken by BOTH student 1 and student 4
SELECT course_id FROM enrollments WHERE student_id = 1
INTERSECT
SELECT course_id FROM enrollments WHERE student_id = 4;

-- INTERSECT emulation for older versions
SELECT DISTINCT e1.course_id
FROM enrollments e1
JOIN enrollments e2 ON e2.course_id = e1.course_id
WHERE e1.student_id = 1 AND e2.student_id = 4;

-- EXCEPT (8.0.31+): courses student 1 took that student 4 did not
SELECT course_id FROM enrollments WHERE student_id = 1
EXCEPT
SELECT course_id FROM enrollments WHERE student_id = 4;

-- EXCEPT emulation
SELECT course_id FROM enrollments
WHERE student_id = 1
  AND course_id NOT IN (SELECT course_id FROM enrollments WHERE student_id = 4);
