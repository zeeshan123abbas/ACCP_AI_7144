# Design Plan: Student Enrollment System

## 1. Requirements (in plain words)
- Students register with name, email (unique), phone, date of birth.
- Courses have a code, title, duration (weeks) and fee.
- Each course is taught by one faculty member; a faculty member can teach many courses.
- A student can enroll in many courses; each enrollment stores date and final marks.
- Fee payments are recorded per enrollment (amount, date, method).

## 2. Entities and attributes
| Entity | Attributes | Primary key |
|---|---|---|
| Student | student_id, full_name, email, phone, dob | student_id |
| Faculty | faculty_id, full_name, email | faculty_id |
| Course | course_id, code, title, weeks, fee, faculty_id | course_id |
| Enrollment | enrollment_id, student_id, course_id, enrolled_on, marks | enrollment_id |
| Payment | payment_id, enrollment_id, amount, paid_on, method | payment_id |

## 3. Relationships
- Faculty 1 — N Course
- Student M — N Course (through Enrollment)
- Enrollment 1 — N Payment

## 4. Business rules / constraints
- email UNIQUE; marks 0–100; fee > 0; method IN ('cash','card','bank')
- A student cannot enroll twice in the same course: UNIQUE(student_id, course_id)

## 5. Normal form check
- [x] 1NF: atomic columns, every table has a PK
- [x] 2NF: no partial dependencies
- [x] 3NF: no transitive dependencies
