-- Create Source Database and Tables
DROP DATABASE IF EXISTS source_db;
CREATE DATABASE source_db;
USE source_db;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);

INSERT INTO employees (id, name, department) VALUES
(1, 'Alice', 'Sales'),
(2, 'Bob', 'IT'),
(3, 'Charlie', 'HR');

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100),
    manager VARCHAR(100)
);

INSERT INTO departments (dept_id, dept_name, manager) VALUES
(1, 'Sales', 'David'),
(2, 'IT', 'Eve'),
(3, 'HR', 'Frank');


-- Create Destination Database
DROP DATABASE IF EXISTS dest_db;
CREATE DATABASE dest_db;
