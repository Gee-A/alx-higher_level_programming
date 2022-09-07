-- creates the database 'hbtn_0d_usa' and table 'states' on MySQL server
-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- create table 
CREATE TABLE IF NOT EXISTS
states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));