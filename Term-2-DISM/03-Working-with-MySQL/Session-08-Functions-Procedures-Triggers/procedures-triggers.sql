-- procedures-triggers.sql
USE institute_db;

-- 1) View: a safe, simple result card
CREATE OR REPLACE VIEW v_result_card AS
SELECT s.full_name, c.title, e.marks,
       CASE WHEN e.marks IS NULL THEN 'PENDING'
            WHEN e.marks >= 50 THEN 'PASS' ELSE 'FAIL' END AS result
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses  c ON c.course_id  = e.course_id;

DELIMITER $$

-- 2) Procedure with IN and OUT parameters
DROP PROCEDURE IF EXISTS sp_student_balance $$
CREATE PROCEDURE sp_student_balance(IN p_student INT, OUT p_due DECIMAL(10,2))
BEGIN
  SELECT COALESCE(SUM(c.fee), 0) - COALESCE((
           SELECT SUM(p.amount) FROM payments p
           JOIN enrollments e2 ON e2.enrollment_id = p.enrollment_id
           WHERE e2.student_id = p_student), 0)
  INTO p_due
  FROM enrollments e JOIN courses c ON c.course_id = e.course_id
  WHERE e.student_id = p_student;
END $$

-- 3) Stored function: grade letter
DROP FUNCTION IF EXISTS fn_grade $$
CREATE FUNCTION fn_grade(p_marks INT) RETURNS CHAR(2)
DETERMINISTIC
BEGIN
  RETURN CASE
    WHEN p_marks IS NULL THEN '-'
    WHEN p_marks >= 85 THEN 'A+'
    WHEN p_marks >= 75 THEN 'A'
    WHEN p_marks >= 65 THEN 'B'
    WHEN p_marks >= 50 THEN 'C'
    ELSE 'F' END;
END $$

-- 4) Audit table + triggers
CREATE TABLE IF NOT EXISTS marks_audit (
  id INT AUTO_INCREMENT PRIMARY KEY,
  enrollment_id INT UNSIGNED,
  old_marks TINYINT UNSIGNED,
  new_marks TINYINT UNSIGNED,
  changed_by VARCHAR(100),
  changed_at DATETIME DEFAULT CURRENT_TIMESTAMP
) $$

DROP TRIGGER IF EXISTS trg_marks_before_update $$
CREATE TRIGGER trg_marks_before_update
BEFORE UPDATE ON enrollments FOR EACH ROW
BEGIN
  IF NEW.marks > 100 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Marks cannot exceed 100';
  END IF;
END $$

DROP TRIGGER IF EXISTS trg_marks_after_update $$
CREATE TRIGGER trg_marks_after_update
AFTER UPDATE ON enrollments FOR EACH ROW
BEGIN
  IF NOT (OLD.marks <=> NEW.marks) THEN
    INSERT INTO marks_audit (enrollment_id, old_marks, new_marks, changed_by)
    VALUES (NEW.enrollment_id, OLD.marks, NEW.marks, CURRENT_USER());
  END IF;
END $$

DELIMITER ;

-- Try it
SELECT * FROM v_result_card;
CALL sp_student_balance(4, @due);
SELECT @due AS amount_due_for_student_4;
SELECT full_name, title, marks, fn_grade(marks) AS grade FROM v_result_card;
UPDATE enrollments SET marks = 52 WHERE enrollment_id = 11;
SELECT * FROM marks_audit;
