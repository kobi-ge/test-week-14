import time
import pandas as pd

from db import DBManager
from models import *

def manager():
    df = load_csv()
    newdf = add_risk_level(df)
    print(df.columns)
    clean_df = clean_null(newdf)
    create_table(db, table_name)
    res = insert_df(clean_df, table_name)
    return res

db = DBManager()
table_name = "weapons_table"

def create_table(db, table_name):
    schema = """
        id INT AUTO_INCREMENT PRIMARY KEY,
        weapon_id VARCHAR(10),
        weapon_name VARCHAR(30),
        weapon_type VARCHAR(30),
        range_km INT,
        weight_kg DECIMAL,
        manufacturer VARCHAR(30),
        origin_country VARCHAR(30),
        storage_location VARCHAR(30),
        year_estimated INT,
        risk_level VARCHAR(30)
    """
    return db.create_table(table_name, schema)

def insert_df(df, table_name):
    columns = "(weapon_id, weapon_name, weapon_type, range_km, weight_kg, manufacturer, origin_country, storage_location, year_estimated, risk_level)"
    values = "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    row_count = 0
    for index, row in df.iterrows():
        query = f"INSERT INTO {table_name} {columns} VALUES {values}"
        row = (row['weapon_id'], row['weapon_name'], row['weapon_type'], row['range_km'], row['weight_kg'], row['manufacturer'], row['origin_country'], row['storage_location'], row['year_estimated'], row['risk_level'])
        db.insert(query, row)
        row_count += 1
    return {
        "status": "success",
        "inserted_records": row_count   
        }

