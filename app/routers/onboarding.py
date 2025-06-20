from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.models.onboarding import UserAnswer

from datetime import datetime

router = APIRouter()

@router.post("/api/bulk-save-answers/")
def bulk_save_answers(payload: dict, db: Session = Depends(get_db)):
    try:
        user_id = payload.get("user_id")
        questions = payload.get("questions", [])

        if not user_id:
            raise HTTPException(status_code=400, detail="Missing user_id.")
        if not questions:
            raise HTTPException(status_code=400, detail="No questions found.")

        for item in questions:
            question_id = item.get("question_id")
            if not question_id:
                continue

            answer_id = item.get("answer_id")
            custom_text = None
            unit_type = item.get("unit_type")
            numeric_value = None

            # 🎯 Handle special case: Height & Weight (Q14)
            if question_id == 14:
                if unit_type == "metric":
                    height_cm = item.get("height_cm")
                    weight_kg = item.get("weight_kg")
                    custom_text = f"{height_cm} cm, {weight_kg} kg"
                    numeric_value = weight_kg  # Optional: can be used later
                elif unit_type == "imperial":
                    height_ft = item.get("height_ft")
                    height_in = item.get("height_in")
                    weight_lb = item.get("weight_lb")
                    custom_text = f"{height_ft}'{height_in}\", {weight_lb} lb"
                    numeric_value = weight_lb  # Optional

            # 🎯 Handle goal weight (Q15)
            elif question_id == 15:
                goal_weight = item.get("goal_weight")
                custom_text = f"{goal_weight} {item.get('unit', '')}"
                numeric_value = goal_weight

            # 🎯 Handle goal timeline (Q16)
            elif question_id == 16:
                result_in_weeks = item.get("result_in_weeks")
                if result_in_weeks:
                    goal_date = datetime.today() + timedelta(weeks=result_in_weeks)
                    custom_text = f"{result_in_weeks} weeks"
                    numeric_value = result_in_weeks
                    item["reach_goal_by"] = goal_date.strftime("%Y-%m-%d")  # For frontend if needed

            # Other fallback types
            elif "answer" in item:
                custom_text = item["answer"]
            elif "value" in item:
                custom_text = str(item["value"])
            elif "answers" in item:
                custom_text = ", ".join(item["answers"])

            # Check if entry already exists
            existing = db.query(UserAnswer).filter_by(user_id=user_id, question_id=question_id).first()

            if existing:
                existing.answer_id = answer_id
                existing.custom_text = custom_text
                existing.unit_type = unit_type
                existing.numeric_value = numeric_value
            else:
                db.add(UserAnswer(
                    user_id=user_id,
                    question_id=question_id,
                    answer_id=answer_id,
                    custom_text=custom_text,
                    unit_type=unit_type,
                    numeric_value=numeric_value
                ))

        db.commit()
        return {"message": "User answers saved successfully ✅"}

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Duplicate or constraint error.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
