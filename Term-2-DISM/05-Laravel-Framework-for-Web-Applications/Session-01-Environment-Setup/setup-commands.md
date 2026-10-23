# Laravel setup checklist (Windows)

1. Install XAMPP 8.2+ and add `C:\xampp\php` to the PATH  ->  `php -v`
2. In `C:\xampp\php\php.ini` enable: `extension=zip`, `extension=fileinfo`, `extension=pdo_mysql`
3. Install Composer (https://getcomposer.org/Composer-Setup.exe)  ->  `composer -V`
4. Install Node.js 20 LTS  ->  `node -v` and `npm -v`
5. Install Git for Windows  ->  `git --version`
6. Create the project:
       composer create-project laravel/laravel student-portal
       cd student-portal
       php artisan --version
       php artisan serve
7. Open http://127.0.0.1:8000 - you should see the Laravel welcome page
8. Open the folder in VS Code: `code .`
9. Initialise Git:
       git init && git add . && git commit -m "Fresh Laravel 11 install"
