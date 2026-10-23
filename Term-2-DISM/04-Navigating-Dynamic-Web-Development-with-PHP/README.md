# Navigating Dynamic Web Development with PHP

![PHP](https://img.shields.io/badge/PHP-8.3-777bb4?logo=php&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-8-4479a1?logo=mysql&logoColor=white) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952b3?logo=bootstrap&logoColor=white) ![Composer](https://img.shields.io/badge/Composer-2-885630?logo=composer&logoColor=white) ![XAMPP](https://img.shields.io/badge/XAMPP-8.2-fb7a24?logo=xampp&logoColor=white)

> Term 2 (DISM) · 18 sessions · ⏱ ~2 hours each

This is the core back-end module of Term 2. You will learn PHP from "Hello World" to a secure, database-driven web application with forms, sessions, file uploads, email, authentication, object-oriented code, JSON APIs and AJAX. Everything you build here prepares you for Laravel (Module 05) and your eProject.

## What You Will Learn

- Set up a local PHP development environment (XAMPP/Laragon, VS Code, Composer)
- Write PHP 8 code: types, strings, operators, regex, conditions, loops, arrays and functions
- Handle forms, cookies, sessions and file uploads securely
- Build full CRUD applications with PDO and MySQL
- Create an admin panel with authentication and role-based authorization
- Send email with PHPMailer
- Write object-oriented PHP with namespaces, traits, interfaces and inheritance
- Build JSON APIs and AJAX features such as live search and a shopping cart

## Prerequisites

- HTML5, CSS3 and Bootstrap basics
- JavaScript fundamentals (Module 02)
- SQL basics (Module 03)

## Tools to Install

| Tool | Purpose | Download |
|---|---|---|
| XAMPP (PHP 8.2+) | Apache + MySQL/MariaDB + PHP | [https://www.apachefriends.org/](https://www.apachefriends.org/) |
| Laragon (alternative) | Lightweight local stack for Windows | [https://laragon.org/](https://laragon.org/) |
| Visual Studio Code | Editor (add the PHP Intelephense extension) | [https://code.visualstudio.com/](https://code.visualstudio.com/) |
| Composer | PHP package manager | [https://getcomposer.org/](https://getcomposer.org/) |
| Postman (optional) | Test HTTP/JSON endpoints | [https://www.postman.com/downloads/](https://www.postman.com/downloads/) |
| Mailtrap (optional) | Safe email testing inbox | [https://mailtrap.io/](https://mailtrap.io/) |

## Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to PHP | [Open notes](./Session-01-Introduction-to-PHP/README.md) |
| 02 | Installing PHP and Basic Syntax | [Open notes](./Session-02-Installation-and-Syntax/README.md) |
| 03 | Data Types, Strings and Constants | [Open notes](./Session-03-Data-Types-Strings-Constants/README.md) |
| 04 | Variables, Scope, Operators and Regular Expressions | [Open notes](./Session-04-Variables-Scope-Operators-RegEx/README.md) |
| 05 | Conditions, Loops and Arrays | [Open notes](./Session-05-Conditions-Loops-Arrays/README.md) |
| 06 | HTML Forms and Validation | [Open notes](./Session-06-Form-Handling-and-Validation/README.md) |
| 07 | Functions in PHP | [Open notes](./Session-07-Functions/README.md) |
| 08 | Cookies and Sessions | [Open notes](./Session-08-Cookies-and-Sessions/README.md) |
| 09 | File Uploading and File Handling | [Open notes](./Session-09-File-Upload-and-Handling/README.md) |
| 10 | PHP and MySQL: Connecting, Creating and Reading | [Open notes](./Session-10-PHP-MySQL-Create-Read/README.md) |
| 11 | PHP and MySQL: Update, Delete and Search | [Open notes](./Session-11-PHP-MySQL-Update-Delete-Search/README.md) |
| 12 | Admin Panel and Dashboard | [Open notes](./Session-12-Admin-Panel-Dashboard/README.md) |
| 13 | Sending Email with PHP | [Open notes](./Session-13-Emailing-with-PHPMailer/README.md) |
| 14 | Authentication and Authorization | [Open notes](./Session-14-Authentication-and-Authorization/README.md) |
| 15 | Object-Oriented PHP: Classes and Objects | [Open notes](./Session-15-OOP-Classes-and-Objects/README.md) |
| 16 | OOP Part 2: Inheritance, Interfaces and Abstract Classes | [Open notes](./Session-16-OOP-Inheritance-Interfaces/README.md) |
| 17 | PHP Web Concepts and JSON | [Open notes](./Session-17-Web-Concepts-and-JSON/README.md) |
| 18 | PHP and AJAX: Live Search and Shopping Cart | [Open notes](./Session-18-PHP-AJAX-Live-Search-Cart/README.md) |

## Module Mini-Project

**Online Book Store (plain PHP).** Combine the sessions into one app:

1. Public pages built from header/footer includes; books loaded from MySQL with search and pagination.
2. User registration/login with hashed passwords, CSRF tokens and roles (admin, customer).
3. Admin panel: dashboard statistics and books CRUD with cover image upload.
4. AJAX live search and a session cart with checkout that stores orders in a transaction.
5. Order confirmation email with PHPMailer.
6. A small JSON API (`api/books.php`) and OOP models (`Book`, `Cart`, `Order`) autoloaded with Composer.

## Resources (Official Documentation)

- [PHP Manual](https://www.php.net/manual/en/)
- [PHP: PDO](https://www.php.net/manual/en/book.pdo.php)
- [PHP: Sessions](https://www.php.net/manual/en/book.session.php)
- [PHP: Password hashing](https://www.php.net/manual/en/book.password.php)
- [PHP: Classes and Objects](https://www.php.net/manual/en/language.oop5.php)
- [PHPMailer on GitHub](https://github.com/PHPMailer/PHPMailer)
- [Composer documentation](https://getcomposer.org/doc/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [MDN: Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

---

[🏠 Term Home](../README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
