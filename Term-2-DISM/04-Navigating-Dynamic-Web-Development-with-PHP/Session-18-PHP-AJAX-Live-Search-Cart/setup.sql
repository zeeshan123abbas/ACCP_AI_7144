-- setup.sql (uses the php_course database from Session 10)
USE php_course;
CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(9,2) NOT NULL
);
INSERT INTO products (name, price) VALUES
 ('PHP 8 Basics (book)', 1800), ('MySQL Pocket Guide', 950), ('Laravel Up and Running', 4200),
 ('JavaScript Cookbook', 2600), ('WordPress for Beginners', 1500);
