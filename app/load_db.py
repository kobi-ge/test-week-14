import time
import pandas as pd

from db import DBManager

df = pd.read_csv("data\weapons_list.csv")

db = DBManager()
table_name = "weapons"

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
        level_risk VARCHAR(30)
    """
    return db.create_table(table_name, schema)

def insert_df(df, table_name):
    columns = "(weapon_id, weapon_name, weapon_type, range_km, weight_kg, manufacturer, origin_country, storage_location, year_estimated, level_risk)"
    values = "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for index, row in df.iterrows():
        query = f"INSERT INTO {table_name} {columns} VALUES {values}"
        db.cursor.execute(query, row)

print(create_table(db, table_name))
insert_df(df, table_name)
# users_schema = """
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(50) NOT NULL,
#     role VARCHAR(20) DEFAULT 'student'
# """
# db.create_table("users", users_schema)

# sql = "INSERT INTO users (username, role) VALUES (%s, %s)"
# db.execute_insert(sql, ("Yossi_Cohen", "Admin"))

# print("app is running...")
# try:
#     while True:
#         time.sleep(60)
# except KeyboardInterrupt:
#     db.close()