# from fastapi import FastAPI
# from db import get_connection

# app = FastAPI(title="Gutendex API")

# @app.get("/")
# def home():
#     return {"message": "Gutendex API is running!"}

# @app.get("/books")
# def get_books():
#     conn = get_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT id, title FROM books_book LIMIT 10;")
#     books = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return {"books": books}


import mysql.connector
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

@app.get("/books")
def get_books():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books_book LIMIT 10;")
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
