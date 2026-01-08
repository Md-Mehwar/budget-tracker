# routers/stats.py
# This file contains all analytics endpoints for the FastAPI service.
# I'm starting with an endpoint that groups totals by category for a given month and user.

from fastapi import APIRouter, HTTPException, Query
from typing import List
from models.schemas import CategoryTotal   # JSON response structure
from db.connect import engine              # Database connection
from sqlalchemy import text
from datetime import date
import calendar

# Creating the router that will hold all analytics routes.
router = APIRouter()

@router.get("/by-category", response_model=List[CategoryTotal])
def by_category(
    month: str = Query(..., description="Month in YYYY-MM format. Example: 2025-12"),
    user_id: int = Query(..., description="User ID whose transactions should be analyzed")
):
    # Parsing and validating the month requested.
    try:
        year_str, month_str = month.split("-")
        year = int(year_str)
        month_num = int(month_str)

        # First day of the month
        start_date = date(year, month_num, 1)

        # Calculate the last day of this month
        last_day = calendar.monthrange(year, month_num)[1]
        end_date = date(year, month_num, last_day)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid month format: {e}")

    # SQL query to sum amounts grouped by category.
    sql = text("""
        SELECT category, COALESCE(SUM(amount), 0) AS total
        FROM transactions
        WHERE user_id = :uid AND date >= :start AND date <= :end
        GROUP BY category
        ORDER BY total DESC;
    """)

    # Running the query inside a try block for safety.
    try:
        with engine.connect() as conn:
            rows = conn.execute(sql, {
                "uid": user_id,
                "start": start_date,
                "end": end_date
            }).all()

        # Converting raw SQL rows into clean JSON response objects.
        results = [
            {
                "category": row[0] if row[0] else "Uncategorized",
                "total": float(row[1] or 0.0)
            }
            for row in rows
        ]

        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
