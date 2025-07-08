# Python MySQL Employee Fetcher

A simple Python script that connects to a MySQL database, retrieves data from an `Employees` table, and prints it to the console. This project demonstrates:


- Error handling for database connections and queries
- Easy setup with `requirements.txt`
- Sample SQL scripts to create and populate the database

---

## Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Project Structure](#project-structure)  
3. [Setup Instructions](#setup-instructions)  
4. [Environment Variables](#environment-variables)  
5. [Running the Script](#running-the-script)  
6. [SQL Setup](#sql-setup)  
7. [Extending This Project](#extending-this-project)  
8. [License](#license)  

---

## Prerequisites

- Python 3.6 or later  
- MySQL Server (local or remote)  
- `pip` package manager  

---

## Project Structure

```
.
├── fetch_employees.py       # Main Python script
├── requirements.txt         # Python dependencies
├── mysql_setup.sql          # SQL to create DB, table, and sample data
└── README.md                # This file
```

---

## Setup Instructions

1. **Clone or download** this repository to your local machine.  
2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows CMD
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## Environment Variables

Create a file named `.env` in the project root with the following contents:

```ini
DB_HOST=localhost
DB_PORT=3306
DB_NAME=CompanyDB
DB_USER=appuser
DB_PASS=StrongPassw0rd!
```

> **Security note:**  
> - Never commit `.env` to your repository.  
> - Add `.env` to `.gitignore`.

---

## Running The Script

Once your environment is active and dependencies installed:

```bash
python fetch_employees.py
```

You should see output similar to:

```
EmployeeID | FirstName | LastName | Title | HireDate | Salary
--------------------------------------------------------------
1          | Alice     | Johnson  | Manager | 2019-03-15 | 85000.00
...
```

---

## SQL Setup

1. **Run** `mysql_setup.sql` to create the `CompanyDB` database, the `Employees` table, and insert sample rows.  
2. **Optionally**, run `add_more_employees.sql` to insert additional records:

```bash
mysql -u root -p < mysql_setup.sql
mysql -u root -p < add_more_employees.sql
```

---

## Extending This Project

- Export query results to CSV or Excel  
- Add filtering, sorting, or pagination  
- Integrate into a web application (e.g., Flask, Django)  
- Add unit tests with `pytest`  

---

## License

This project is released under the MIT License.
