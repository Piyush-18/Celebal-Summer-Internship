# MySQL Data Integration & Export Pipeline with Airflow

This project demonstrates how to build a Python-based data pipeline that extracts data from a source MySQL database, exports it to multiple file formats (CSV, Parquet, and Avro), and optionally loads it into a destination MySQL database. The pipeline can be automated using Apache Airflow or scheduled manually via cron or Task Scheduler.

---

## 🚀 Features

- 🔌 Connects to MySQL databases using SQLAlchemy + PyMySQL
- 📤 Exports data to:
  - CSV (easy to read)
  - Parquet (columnar, efficient for big data)
  - Avro (binary + schema)
- 🔁 Copies data from source DB to destination DB (table-by-table)
- 📅 Optional: Schedule automation using Airflow, cron, or Windows Task Scheduler
- 🧪 Structured for easy testing and modularization

---

## 📁 Project Structure

```
mysql_data_pipeline/
│
├── main.py                  # Main pipeline runner
├── config.py                # Reads MySQL config from .env
├── requirements.txt         # All dependencies
├── .env                     # Environment variables (DB credentials)
│
├── utils/
│   ├── db.py                # DB connection and fetch logic
│   └── export.py            # Export logic (CSV, Parquet, Avro)
│
├── output/                  # Exported files go here
│
└── dags/
    └── daily_pipeline.py    # Airflow DAG to schedule the pipeline
```

---

## 🔧 Requirements

- Python 3.7 or 3.8
- MySQL server running locally or remotely
- Virtualenv or Conda (recommended)
- [Apache Airflow (optional)](https://airflow.apache.org/docs/)

---

## ✅ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mysql-data-pipeline.git
cd mysql-data-pipeline
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
.env\Scriptsctivate    # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 .env File Example

Create a file named `.env` and add:

```
SOURCE_USER=root
SOURCE_PASSWORD=your_password
SOURCE_HOST=localhost
SOURCE_PORT=3306
SOURCE_DATABASE=source_db

DEST_USER=root
DEST_PASSWORD=your_password
DEST_HOST=localhost
DEST_PORT=3306
DEST_DATABASE=dest_db
```

---

## ▶️ Run the Pipeline Manually

```bash
python main.py
```

This will:
- Export each table to `/output/*.csv`, `.parquet`, `.avro`
- Copy the same data to the destination database

---

## 🛠 Automate with Airflow 

### 1. Set environment variable before running Airflow

```powershell
$env:AIRFLOW_HOME = "F:/your/path/to/airflow_home"
$env:AIRFLOW__DATABASE__SQL_ALCHEMY_CONN = "sqlite:///F:/your/path/to/airflow_home/airflow.db"
```

### 2. Initialize Airflow DB

```bash
airflow db init
```

### 3. Create Airflow user

```bash
airflow users create --username admin --password admin123 --firstname Admin --lastname User --role Admin --email admin@example.com
```

### 4. Start services

```bash
airflow scheduler
airflow webserver --port 8080
```

Visit [http://localhost:8080](http://localhost:8080)

---

## ⏰ Automate with Task Scheduler (Windows)

1. Open **Task Scheduler**
2. Create Basic Task → Trigger: Daily → Action: Start a Program
3. Program: `python`
4. Arguments: `main.py`
5. Start in: Full path to the project folder

---

## 📬 Contact

Maintainer: Piyush  
Feel free to submit issues or pull requests!

