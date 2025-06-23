from utils.db import get_engine, fetch_table
from utils.export import export_all_formats
from config import SOURCE_DB, DEST_DB
import pandas as pd

source_engine = get_engine(SOURCE_DB)
dest_engine = get_engine(DEST_DB)

tables = ['employees', 'departments']
for table in tables:
    df = fetch_table(source_engine, table)
    export_all_formats(df, table)
    df.to_sql(table, dest_engine, index=False, if_exists='replace')
