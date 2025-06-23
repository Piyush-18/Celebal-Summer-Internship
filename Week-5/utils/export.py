import pandas as pd
from fastavro import writer, parse_schema
import os

def export_all_formats(df, table_name):
    os.makedirs("output", exist_ok=True)
    df.to_csv(f"output/{table_name}.csv", index=False)
    df.to_parquet(f"output/{table_name}.parquet", index=False)

    schema = {
        "name": table_name,
        "type": "record",
        "fields": [{"name": col, "type": "string"} for col in df.columns]
    }
    parsed_schema = parse_schema(schema)
    records = df.astype(str).to_dict(orient="records")

    with open(f"output/{table_name}.avro", "wb") as out:
        writer(out, parsed_schema, records)
