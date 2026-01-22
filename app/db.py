import mysql.connector
from mysql.connector import Error
import os


class DBManager:
    def __init__(self):
        self._load_config()
        self.connection = None
        self.cursor = None
        self.initialize_connection_flow()
    
    def _load_config(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.db_name = os.getenv("DB_NAME", "weapons_db")

    def initialize_connection_flow(self):
        if self._connect_to_server():
            self._ensure_database_exists()
            self._select_database()

    def _connect_to_server(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("connected to MySQL Server.")
                return True
        except Error as e:
            print(f"connection failed: {e}")
            return False
        
    def _ensure_database_exists(self):
        try:
            query = f"CREATE DATABASE IF NOT EXISTS {self.db_name}"
            self.cursor.execute(query)
            print(f"database '{self.db_name}' verified.")
        except Error as e:
            print(f"failed to create database: {e}")

    def _select_database(self):
        try:
            self.connection.database = self.db_name
            print(f"selected database: {self.db_name}")
        except Error as e:
            print(f"failed to select database: {e}")
    
    def create_table(self, table_name, columns_schema):
        if not self.connection: 
            return "connection failed"
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_schema})"
            self.cursor.execute(query)
            self.connection.commit() 
            print(f"table '{table_name}' is ready.")
        except Error as e:
            print(f"table creation failed: {e}")

    def insert(self, query, values):
        if not self.connection: 
            return "connection failed"
        try:
            self.cursor.execute(query, values)
            self.connection.commit() 
            print("data inserted successfully.")
        except Error as e:
            print(f"insert failed: {e}")

    def close(self):
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("connection closed.")


