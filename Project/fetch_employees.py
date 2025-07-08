import mysql.connector
from mysql.connector import Error

# 1. Connection parameters
HOST     = 'localhost'      
PORT     = 3306             
DATABASE = 'CompanyDB'
USERNAME = 'root'
PASSWORD = '<Piyush@18>'

def fetch_employees(limit=5):
    """
    Connects to MySQL, retrieves the first `limit` rows
    from Employees, and prints them out.
    """
    try:
        conn = mysql.connector.connect(
            host=HOST,
            port=PORT,
            database=DATABASE,
            user=USERNAME,
            password=PASSWORD,
            connect_timeout=5
        )
        if not conn.is_connected():
            print("[ERROR] Connection failed.")
            return
    except Error as e:
        print(f"[ERROR] Could not connect to MySQL: {e}")
        return

    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Employees LIMIT {limit};")
        rows = cursor.fetchall()

        if not rows:
            print("No rows found in Employees table.")
            return

        # Print header
        cols = [desc[0] for desc in cursor.description]
        print(" | ".join(cols))
        print("-" * (len(cols) * 15))

        # Print each row
        for row in rows:
            print(" | ".join(str(val) for val in row))

    except Error as e:
        print(f"[ERROR] Query failed: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    fetch_employees()
