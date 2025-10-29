from fastapi import FastAPI
from db import get_connection

app = FastAPI(title="Gutendex API")

@app.get("/")
def home():
    return {"message": "Gutendex API is running!"}

@app.get("/books")
def get_books():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, title FROM books_book LIMIT 10;")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"books": books}
