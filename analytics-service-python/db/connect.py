# analytics-service-python/db/connect.py

import sqlite3
import os

# Always use absolute path so FastAPI does not get confused
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "analytics.db")

DB_PATH = os.path.abspath(DB_PATH)

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Create transactions table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()

# Run table creation immediately
init_db()
