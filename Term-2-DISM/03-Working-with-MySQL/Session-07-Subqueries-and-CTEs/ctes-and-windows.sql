-- ctes-and-windows.sql  (MySQL 8.0+)
USE institute_db;

-- Named steps with WITH
WITH course_avg AS (
  SELECT course_id, AVG(marks) AS avg_marks
  FROM enrollments WHERE marks IS NOT NULL
  GROUP BY course_id
)
SELECT c.title, ROUND(ca.avg_marks, 1) AS avg_marks
FROM course_avg ca JOIN courses c ON c.course_id = ca.course_id
ORDER BY avg_marks DESC;

-- Recursive CTE: the 12 months of 2025 (useful for reports with empty months)
WITH RECURSIVE months AS (
  SELECT DATE('2025-01-01') AS m
  UNION ALL
  SELECT m + INTERVAL 1 MONTH FROM months WHERE m < '2025-12-01'
)
SELECT DATE_FORMAT(m, '%b %Y') AS month,
       COALESCE((SELECT SUM(amount) FROM payments
                 WHERE DATE_FORMAT(paid_on, '%Y-%m') = DATE_FORMAT(m, '%Y-%m')), 0) AS collected
FROM months;

-- Window functions: rank students inside each course
SELECT c.title, s.full_name, e.marks,
       RANK() OVER (PARTITION BY e.course_id ORDER BY e.marks DESC) AS position
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses  c ON c.course_id  = e.course_id
WHERE e.marks IS NOT NULL;

-- Running total of collections by date
SELECT DATE(paid_on) AS day, SUM(amount) AS collected,
       SUM(SUM(amount)) OVER (ORDER BY DATE(paid_on)) AS running_total
FROM payments
GROUP BY DATE(paid_on);
