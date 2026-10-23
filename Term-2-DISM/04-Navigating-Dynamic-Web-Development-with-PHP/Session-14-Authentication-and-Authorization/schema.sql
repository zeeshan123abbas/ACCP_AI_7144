-- schema.sql : run once in phpMyAdmin or MySQL Workbench
CREATE DATABASE IF NOT EXISTS php_course CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE php_course;

CREATE TABLE IF NOT EXISTS students (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  name       VARCHAR(100) NOT NULL,
  email      VARCHAR(120) NOT NULL UNIQUE,
  course     VARCHAR(60)  NOT NULL,
  city       VARCHAR(50)  NOT NULL DEFAULT 'Karachi',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS users (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  name       VARCHAR(100) NOT NULL,
  email      VARCHAR(120) NOT NULL UNIQUE,
  password   VARCHAR(255) NOT NULL,          -- password_hash() output
  role       ENUM('admin','user') NOT NULL DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT IGNORE INTO students (name, email, course, city) VALUES
 ('Ayesha Khan','ayesha@mail.com','PHP','Karachi'),
 ('Bilal Ahmed','bilal@mail.com','MySQL','Hyderabad'),
 ('Sana Javed','sana@mail.com','Laravel','Karachi'),
 ('Usman Ali','usman@mail.com','JavaScript','Lahore');

-- Promote yourself after registering:
-- UPDATE users SET role = 'admin' WHERE email = 'you@example.com';
