CREATE DATABASE cyber_security_db;
USE cyber_security_db;


CREATE TABLE ThreatLogs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_ip VARCHAR(50),
    event_type VARCHAR(50), -- e.g., 'DDoS', 'SQL Injection', 'Brute Force'
    severity_level INT,     -- 1 (Low) to 5 (Critical)
    asset_criticality INT,  -- 1 (Laptop) to 10 (Main Database)
    description TEXT
);

-- Adding some dummy data to see results immediately
INSERT INTO ThreatLogs (source_ip, event_type, severity_level, asset_criticality, description)
VALUES 
('192.168.1.105', 'Brute Force', 4, 8, 'Multiple failed SSH attempts'),
('10.0.0.50', 'SQL Injection', 5, 9, 'Attempted UNION SELECT on login form'),
('172.16.254.1', 'Port Scan', 2, 3, 'Nmap scan detected on peripheral subnet');

select * from Threatlogs;

ALTER TABLE ThreatLogs
ADD COLUMN risk_score INT;
DESCRIBE ThreatLogs;

ALTER TABLE ThreatLogs
ADD COLUMN country VARCHAR(100),
ADD COLUMN city VARCHAR(100),
ADD COLUMN isp VARCHAR(150),
ADD COLUMN organization VARCHAR(150);

DESCRIBE ThreatLogs;


USE cyber_security_db;


CREATE TABLE Users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(50) UNIQUE,

    password VARCHAR(255),

    role VARCHAR(20)

);

INSERT INTO Users
(username,password,role)
VALUES

('admin','admin123','Admin'),

('analyst','analyst123','SOC Analyst'),

('viewer','viewer123','Viewer');

UPDATE Users
SET password='$2b$12$0n7JV05kLIDwsAq.tSgDlepl/KSMkgpvGCWQBY0iGQ2INj7DDyY9u'
WHERE username='admin';

USE cyber_security_db;

UPDATE Users
SET password='$2b$12$GA3X6p7lGyELXLHVTn.qquNveol12m0f26Lp9ih0yGXyZcxpp2PKe'
WHERE username='analyst';

UPDATE Users
SET password='$2b$12$sle1X7uR2ujiph/5WoR6FuyptNPUBUy6ga4OYe.AsF5H1fKXz0Nh2'
WHERE username='viewer';

SELECT * FROM Users;


USE cyber_security_db;


CREATE TABLE Incidents (

    incident_id INT AUTO_INCREMENT PRIMARY KEY,

    threat_id INT,

    source_ip VARCHAR(50),

    attack_type VARCHAR(100),

    severity INT,

    risk_score INT,

    status VARCHAR(30) DEFAULT 'OPEN',

    assigned_to VARCHAR(50),

    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    resolved_time TIMESTAMP NULL

);

SHOW TABLES;

SELECT * FROM Incidents;


