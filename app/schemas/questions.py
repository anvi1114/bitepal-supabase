from pydantic import BaseModel

class QuestionCreateSchema(BaseModel):
    question_text: str
    question_type: str
    subheading: str | None = None

class QuestionSchema(QuestionCreateSchema):
    id: int

    class Config:
        orm_mode = True
