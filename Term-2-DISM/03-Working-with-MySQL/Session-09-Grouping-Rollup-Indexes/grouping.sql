-- grouping.sql
USE institute_db;

-- Students per city
SELECT city, COUNT(*) AS students
FROM students
GROUP BY city
ORDER BY students DESC;

-- Course statistics, only courses with at least 3 graded students
SELECT c.title, COUNT(e.marks) AS graded, ROUND(AVG(e.marks),1) AS avg_marks,
       MIN(e.marks) AS lowest, MAX(e.marks) AS highest
FROM courses c JOIN enrollments e ON e.course_id = c.course_id
GROUP BY c.title
HAVING COUNT(e.marks) >= 3;

-- Collections by method and month, with subtotals and grand total
SELECT IF(GROUPING(method), 'ALL METHODS', method)              AS method,
       IF(GROUPING(ym), 'Subtotal', ym)                         AS month,
       SUM(amount)                                              AS collected
FROM (SELECT method, DATE_FORMAT(paid_on, '%Y-%m') AS ym, amount FROM payments) p
GROUP BY method, ym WITH ROLLUP;
