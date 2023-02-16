-- a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
CREATE TABLE IF NOT EXIST hbtn_0d_usa.cities(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256),s
	state_id INT NOT NULL, FOREIGN KEY (states) REFERENCES states(id));
