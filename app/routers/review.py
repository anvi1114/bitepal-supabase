from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models.review import UserReview
from app.schemas.reviews import ReviewCreate


router = APIRouter(prefix="/reviews", tags=["Reviews"])

from app.schemas.reviews import ReviewCreate  # make sure this is defined

@router.post("/submit/")
def submit_review(payload: ReviewCreate, db: Session = Depends(get_db)):
    try:
        username = payload.username or "Anonymous"
        content = payload.content
        rating = payload.rating

        if not content or rating is None:
            raise HTTPException(status_code=400, detail="Content and rating are required.")

        review = UserReview(username=username, content=content, rating=rating)
        db.add(review)
        db.commit()

        return {"message": "Review submitted successfully"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/get_all/")
def get_all_reviews(db: Session = Depends(get_db)):
    reviews = db.query(UserReview).all()
    result = [
        {
            "id": r.id,
            "username": r.username,
            "content": r.content,
            "rating": str(r.rating)
        } for r in reviews
    ]

    return {
        "message": "Reviews retrieved successfully",
        "data": result
    }

@router.get("/get_average/")
def get_average_rating(db: Session = Depends(get_db)):
    total_reviews = db.query(UserReview).count()
    average_rating = db.query(func.avg(UserReview.rating)).scalar() or 0.0

    return {
        "message": "Average rating retrieved successfully",
        "data": {
            "average_rating": f"{round(average_rating, 1)}",
            "total_reviews": total_reviews
        }
    }
