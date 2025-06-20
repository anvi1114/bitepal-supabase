from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import UniqueConstraint

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_text = Column(String)
    question_type = Column(String)
    subheading = Column(String, nullable=True)

    answers = relationship("Answer", back_populates="question")


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer_text = Column(String)
    subheading = Column(String, nullable=True)

    question = relationship("Question", back_populates="answers")

class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_profiles.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer_id = Column(Integer, ForeignKey("answers.id"), nullable=True)
    custom_text = Column(String, nullable=True)
    unit_type = Column(String, nullable=True)  # NEW
    numeric_value = Column(Float, nullable=True)  # Optional, for clean BMI

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    # You can add more fields if needed
