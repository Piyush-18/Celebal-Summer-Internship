from sqlalchemy import create_engine
import pandas as pd

def get_engine(db_config):
    return create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

def fetch_table(engine, table_name):
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)
