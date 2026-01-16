import sqlite3

# Connect to DB
conn = sqlite3.connect("analytics.db")
cur = conn.cursor()

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        category TEXT,
        amount REAL,
        date TEXT
    );
""")

# Sample data
sample_data = [
    (1, "Food", 1200, "2025-12-05"),
    (1, "Travel", 500, "2025-12-10"),
    (1, "Shopping", 300, "2025-12-15"),
    (1, "Food", 700, "2025-12-20"),
]

# Insert sample data
for user_id, category, amount, date in sample_data:
    cur.execute("INSERT INTO transactions (user_id, category, amount, date) VALUES (?, ?, ?, ?)",
                (user_id, category, amount, date))

conn.commit()
conn.close()

print("Sample transactions inserted!")
