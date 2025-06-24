from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class UserReview(Base):
    __tablename__ = "user_reviews"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    content = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
