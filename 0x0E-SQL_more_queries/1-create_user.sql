-- creates the MySQL server user user_0d_1 having all privileges
-- user_0d_1 password should be set to user_0d_1_pwd

-- creates a new user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- grants privileges
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;