# db/connect.py
# This file sets up the database connection for the analytics service.
# I'm using SQLite because it's simple and works without any server setup.

from sqlalchemy import create_engine

# SQLite database file stored locally inside the Codespace.
DB_URL = "sqlite:///./analytics.db"

# Creating the SQLite engine. 
engine = create_engine(
    DB_URL,
    echo=True,    # Shows SQL logs in terminal for debugging
    future=True
)
