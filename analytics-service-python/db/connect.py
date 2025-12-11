# db/connect.py
# This file sets up the database connection for my analytics service.
# I'm using SQLAlchemy so I can run SQL queries easily.
# The database URL is read from an environment variable so I can change DBs without changing code.

from sqlalchemy import create_engine
import os

# Reading the DB URL from an environment variable named DB_URL.
# If DB_URL isn't set, I'll use a fallback URL (replace this with your actual DB later).
DB_URL = os.getenv("DB_URL", "postgresql://youruser:yourpassword@localhost:5432/yourdb")

# Creating the SQLAlchemy engine.
# This engine will be used by all analytics endpoints to interact with the database.
engine = create_engine(DB_URL, echo=False, future=True)
