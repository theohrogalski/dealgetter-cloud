import os
from google.cloud.sql.connector import Connector, IPTypes
import pg8000
import requests
import sqlalchemy
import dotenv
from dotenv import load_dotenv
import datetime
load_dotenv()

connector = Connector()

def get_connection():
    return connector.connect(
        instance_connection_string="dealgetter:us-central1:dealgetterpostgresql",  # Replace with your Cloud SQL instance connection name
        driver="pg8000",                         # Database driver
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        db=os.getenv("DB_NAME"),)

# Example usage
def create_table():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS textdata (
            id SERIAL PRIMARY KEY,
            textdata TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """) 
        conn.commit()
    print("BASIC TABLE CREATED OR ALREADY EXISTS\n")
# Close the connector when you're done

def insert_data(data):
    print("started insert")
    with get_connection() as conn:
        print("cursor set")
        cur = conn.cursor()
        print("got curr")
        cur.execute("""
        INSERT INTO textdata (textdata,created_at)
        VALUES (%s,%s)
        """, (data, datetime.datetime.now()))
        print("inserted data")
        conn.commit()
    connector.close()
    print("GOOD TO EXIST")

