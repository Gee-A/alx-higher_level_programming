-- convert a database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in MySQL server
USE `hbtn_0c_0`
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
