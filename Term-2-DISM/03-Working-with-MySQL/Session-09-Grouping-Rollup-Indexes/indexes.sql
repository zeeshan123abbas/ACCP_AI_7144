-- indexes.sql
USE institute_db;

SHOW INDEX FROM students;

-- Before: full scan on city
EXPLAIN SELECT full_name FROM students WHERE city = 'Karachi';

CREATE INDEX idx_students_city ON students(city);

-- After: uses idx_students_city (type = ref)
EXPLAIN SELECT full_name FROM students WHERE city = 'Karachi';

-- Composite index: helps WHERE course_id = ? AND marks >= ?
CREATE INDEX idx_enr_course_marks ON enrollments(course_id, marks);
EXPLAIN SELECT student_id FROM enrollments WHERE course_id = 3 AND marks >= 70;
-- Leftmost-prefix rule: this one cannot use it efficiently
EXPLAIN SELECT student_id FROM enrollments WHERE marks >= 70;

-- Full-text search on course titles
ALTER TABLE courses ADD FULLTEXT INDEX ft_course_title (title);
SELECT title FROM courses WHERE MATCH(title) AGAINST ('web development');

-- Clean up
DROP INDEX idx_students_city ON students;
