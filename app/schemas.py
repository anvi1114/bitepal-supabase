from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

# ✅ Enum for valid question types
class QuestionTypeEnum(str, Enum):
    single_mcq = 'single_mcq'
    multiple_mcq = 'multiple_mcq'
    image = 'image'
    image_content = 'image-content'
    age = 'Age'
    height_weight = 'height_weight'
    desired_weight = 'desired_weight'
    goal = 'goal'
    notification = 'notification'
    image_celebration = 'image-celebration'
    health_benefits = 'health_benefits'

# ✅ Schema to receive each answer
class AnswerCreateSchema(BaseModel):
    answer_text: str
    subheading: Optional[str] = None

# ✅ Schema to create a question
class QuestionCreateSchema(BaseModel):
    question_text: str
    question_type: QuestionTypeEnum  # 👈 this gives Swagger a dropdown 💫
    subheading: Optional[str] = None
    answers: List[AnswerCreateSchema]

# ✅ Schema to return each answer from DB
class AnswerSchema(AnswerCreateSchema):
    id: int

    class Config:
        orm_mode = True

# ✅ Schema to return question + answers from DB
class QuestionSchema(QuestionCreateSchema):
    id: int
    answers: List[AnswerSchema]

    class Config:
        orm_mode = True
