-- subqueries.sql  (run after institute-schema.sql and seed-data.sql)
USE institute_db;

-- Scalar subquery: courses that cost more than the average fee
SELECT code, title, fee
FROM courses
WHERE fee > (SELECT AVG(fee) FROM courses);

-- IN: students who have paid at least once by card
SELECT full_name FROM students
WHERE student_id IN (
  SELECT e.student_id
  FROM enrollments e JOIN payments p ON p.enrollment_id = e.enrollment_id
  WHERE p.method = 'card');

-- NOT EXISTS: students with no enrollment at all
SELECT s.full_name FROM students s
WHERE NOT EXISTS (SELECT 1 FROM enrollments e WHERE e.student_id = s.student_id);

-- Correlated: enrollments scoring above their own course average
SELECT e.student_id, e.course_id, e.marks
FROM enrollments e
WHERE e.marks > (SELECT AVG(e2.marks) FROM enrollments e2 WHERE e2.course_id = e.course_id);

-- Derived table: average amount paid per student
SELECT ROUND(AVG(total_paid)) AS avg_paid_per_student
FROM (
  SELECT e.student_id, SUM(p.amount) AS total_paid
  FROM enrollments e JOIN payments p ON p.enrollment_id = e.enrollment_id
  GROUP BY e.student_id
) AS t;

-- Scalar subquery in SELECT: number of courses per student
SELECT s.full_name,
       (SELECT COUNT(*) FROM enrollments e WHERE e.student_id = s.student_id) AS courses_taken
FROM students s;
