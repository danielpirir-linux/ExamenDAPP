DROP DATABASE IF EXISTS Restaurante_db;
CREATE DATABASE Restaurante_db;
USE Restaurante_db;

CREATE TABLE Platillo(
	IdPlatillo INT auto_increment NOT NULL PRIMARY KEY,
    NombrePlatillo VARCHAR (100) NOT NULL
    );
    
SELECT * FROM Platillo; 