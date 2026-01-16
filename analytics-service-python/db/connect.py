import os
from sqlalchemy import create_engine

# Get current directory (analytics-service-python/db)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one folder to analytics-service-python/
DB_PATH = os.path.join(BASE_DIR, "..", "analytics.db")

# Create engine with absolute path
engine = create_engine(f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False})
