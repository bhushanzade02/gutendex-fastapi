# import mysql.connector
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def get_connection():
#     connection = mysql.connector.connect(
#         host=os.getenv("DB_HOST"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         database=os.getenv("DB_NAME"),
#         port=os.getenv("DB_PORT")
#     )
#     return connection


# from dotenv import load_dotenv
# import os
# import mysql.connector

# load_dotenv()

# # 👇 TEMP: check values
# print("🔍 Loaded DB_HOST:", os.getenv("DB_HOST"))
# print("🔍 Loaded DB_PORT:", os.getenv("DB_PORT"))

# def get_connection():
#     connection = mysql.connector.connect(
#         host=os.getenv("DB_HOST"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         database=os.getenv("DB_NAME"),
#         port=os.getenv("DB_PORT")
#     )
#     return connection



import mysql.connector
from dotenv import load_dotenv
import os
from pathlib import Path

# Force load .env explicitly from the current directory
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

print("🔍 Loaded DB_HOST:", os.getenv("DB_HOST"))
print("🔍 Loaded DB_PORT:", os.getenv("DB_PORT"))

def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")
    )
    return connection
