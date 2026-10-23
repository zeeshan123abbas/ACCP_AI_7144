-- json-and-engines.sql
USE institute_db;

CREATE TABLE student_profiles (
  student_id INT UNSIGNED PRIMARY KEY,
  prefs JSON NOT NULL,
  lang VARCHAR(10) AS (prefs->>'$.language') STORED,   -- generated column
  INDEX idx_lang (lang)
) ENGINE = InnoDB;

INSERT INTO student_profiles (student_id, prefs) VALUES
 (1, '{"language":"en","dark_mode":true,"skills":["php","mysql"]}'),
 (2, '{"language":"ur","dark_mode":false,"skills":["js"]}');

SELECT student_id, prefs->>'$.language' AS language, JSON_LENGTH(prefs->'$.skills') AS skill_count
FROM student_profiles;

SELECT student_id FROM student_profiles WHERE lang = 'ur';   -- uses idx_lang

-- MEMORY engine for a temporary lookup (lost on restart)
CREATE TABLE city_codes (city VARCHAR(30) PRIMARY KEY, code CHAR(3)) ENGINE = MEMORY;
INSERT INTO city_codes VALUES ('Karachi','KHI'), ('Lahore','LHE'), ('Islamabad','ISB');
SELECT s.full_name, cc.code FROM students s LEFT JOIN city_codes cc ON cc.city = s.city;
