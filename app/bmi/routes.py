from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.database import get_db
from app.models.onboarding import UserAnswer
from app.bmi.logic import fetch_bmi_goal_info

router = APIRouter(prefix="/bmi", tags=["BMI"])

@router.get("/goal-info/")
def get_goal_info(user_id: int, db: Session = Depends(get_db)):
    try:
        return fetch_bmi_goal_info(user_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
