# routers/stats.py
# This file contains all analytics endpoints for the FastAPI service.
# It calculates total spending per category for a given month and user.

from fastapi import APIRouter, HTTPException, Query
from typing import List
from models.schemas import CategoryTotal
from db.connect import engine
from sqlalchemy import text
from datetime import date
import calendar

router = APIRouter()

@router.get("/by-category", response_model=List[CategoryTotal])
def by_category(
    month: str = Query(..., description="Month in YYYY-MM format. Example: 2025-12"),
    user_id: int = Query(..., description="User ID whose transactions should be analyzed")
):
    # Parse month input
    try:
        year_str, month_str = month.split("-")
        year = int(year_str)
        month_num = int(month_str)

        start_date = date(year, month_num, 1)
        last_day = calendar.monthrange(year, month_num)[1]
        end_date = date(year, month_num, last_day)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid month format: {e}")

    # SQL query for total spending by category
    sql = text("""
        SELECT category, COALESCE(SUM(amount), 0) AS total
        FROM transactions
        WHERE user_id = :uid
          AND date >= :start
          AND date <= :end
        GROUP BY category
        ORDER BY total DESC;
    """)

    try:
        with engine.connect() as conn:
            rows = conn.execute(sql, {
                "uid": user_id,
                "start": start_date.isoformat(),
                "end": end_date.isoformat()
            }).fetchall()

        results = [
            {"category": row[0] if row[0] else "Uncategorized", "total": float(row[1] or 0)}
            for row in rows
        ]

        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
