-- create a dedicated mysql user with all the permisions. create a database in the root user and give full access to the database to campus CampusNook called CampusNook and with a password of CampusNook.
-- The user is called CampusNook and the password is CampusNook.
CREATE DATABASE CampusNook;
CREATE USER 'CampusNook'@'localhost' IDENTIFIED BY 'CampusNook';
GRANT ALL PRIVILEGES ON CampusNook.* TO 'CampusNook'@'localhost';
FLUSH PRIVILEGES;

