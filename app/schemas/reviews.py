from pydantic import BaseModel, Field

class ReviewCreate(BaseModel):
    username: str = Field(default="Anonymous")
    content: str
    rating: float
