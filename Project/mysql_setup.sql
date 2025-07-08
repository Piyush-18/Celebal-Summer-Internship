-- 1. Create database
CREATE DATABASE IF NOT EXISTS CompanyDB;
USE CompanyDB;

-- 2. Create Employees table
DROP TABLE IF EXISTS Employees;
CREATE TABLE Employees (
    EmployeeID   INT            AUTO_INCREMENT PRIMARY KEY,
    FirstName    VARCHAR(50)    NOT NULL,
    LastName     VARCHAR(50)    NOT NULL,
    Title        VARCHAR(100),
    HireDate     DATE,
    Salary       DECIMAL(10,2)
);

-- 3. Insert sample data
INSERT INTO Employees (FirstName, LastName, Title, HireDate, Salary) VALUES
 ('Alice',   'Johnson',  'Manager',      '2019-03-15', 85000.00),
 ('Bob',     'Smith',    'Engineer',     '2020-07-22', 65000.00),
 ('Carol',   'Williams', 'Analyst',      '2021-01-10', 62000.00),
 ('David',   'Brown',    'Technician',   '2022-09-30', 55000.00),
 ('Eve',     'Davis',    'Accountant',   '2023-05-05', 60000.00),
 ('Frank',   'Miller',   'HR Specialist',     '2023-08-01', 58000.00),
 ('Grace',   'Lee',      'Marketing Lead',    '2022-11-12', 63000.00),
 ('Heidi',   'Clark',    'Consultant',        '2020-02-20', 70000.00),
 ('Ivan',    'Wong',     'DevOps Engineer',   '2021-06-15', 72000.00),
 ('Judy',    'Martinez', 'UI/UX Designer',    '2024-01-05', 54000.00);
