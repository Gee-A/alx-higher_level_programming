-- creates the database 'hbtn_0d_usa' and the table 'cities' on MySQL server

-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_Id) REFERENCES states(id));
