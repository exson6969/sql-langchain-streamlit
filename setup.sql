-- Create the database
CREATE DATABASE company_db;

-- Use the database
USE company_db;

-- Create 'departments' table
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL
);

-- Create 'employees' table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    department_id INT NOT NULL,
    hire_date DATE NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create 'projects' table
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

-- Create 'employee_projects' table to track which employees are working on which projects
CREATE TABLE IF NOT EXISTS employee_projects (
    employee_id INT NOT NULL,
    project_id INT NOT NULL,
    role VARCHAR(255) NOT NULL,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Insert data into 'departments' table
INSERT INTO departments (department_name) VALUES
    ('Engineering'),
    ('Human Resources'),
    ('Marketing'),
    ('Finance');

-- Insert data into 'employees' table
INSERT INTO employees (first_name, last_name, department_id, hire_date, salary) VALUES
    ('Alice', 'Johnson', 1, '2020-06-15', 75000.00),
    ('Bob', 'Smith', 2, '2018-03-10', 60000.00),
    ('Charlie', 'Brown', 3, '2019-07-22', 65000.00),
    ('David', 'Lee', 1, '2021-09-01', 80000.00),
    ('Eve', 'Davis', 4, '2017-01-25', 90000.00);

-- Insert data into 'projects' table
INSERT INTO projects (project_name, start_date, end_date) VALUES
    ('Project Alpha', '2023-01-01', '2023-12-31'),
    ('Project Beta', '2022-06-01', '2023-06-01'),
    ('Project Gamma', '2023-02-15', '2024-02-15');

-- Insert data into 'employee_projects' table
INSERT INTO employee_projects (employee_id, project_id, role) VALUES
    (1, 1, 'Developer'),
    (2, 2, 'HR Manager'),
    (3, 3, 'Marketing Lead'),
    (4, 1, 'Senior Developer'),
    (5, 2, 'Financial Analyst');