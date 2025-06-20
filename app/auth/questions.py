from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas import QuestionCreateSchema, QuestionSchema
from app.supabase_client import supabase

router = APIRouter()

# ✅ GET API - Fetch questions and answers
@router.get("/api/questions", response_model=list[QuestionSchema])
def get_questions():
    try:
        questions_response = supabase.table("questions").select("*").execute()
        answers_response = supabase.table("answers").select("*").execute()

        if not questions_response.data:
            raise HTTPException(status_code=404, detail="No questions found")

        questions_data = questions_response.data
        answers_data = answers_response.data

        # Group answers by question_id
        answer_map = {}
        for answer in answers_data:
            qid = answer["question_id"]
            answer_map.setdefault(qid, []).append(answer)

        # Attach answers to each question
        for question in questions_data:
            qid = question["id"]
            question["answers"] = answer_map.get(qid, [])

        return questions_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching questions: {str(e)}")


# ✅ POST API - Create a new question and its answers
@router.post("/api/questions")
def create_question(question: QuestionCreateSchema):
    try:
        # Step 1: Insert the question
        question_payload = {
            "question_text": question.question_text,
            "question_type": question.question_type,
            "subheading": question.subheading,
        }

        question_response = supabase.table("questions").insert(question_payload).execute()

        if not question_response.data:
            raise HTTPException(status_code=400, detail="Failed to insert question")

        # Step 2: Get inserted question ID
        question_id = question_response.data[0]["id"]

        # Step 3: Insert answers (🚫 no ID passed!)
        answer_payloads = [
            {
                "question_id": question_id,
                "answer_text": ans.answer_text,
                "subheading": ans.subheading,
            }
            for ans in question.answers
        ]

        answer_response = supabase.table("answers").insert(answer_payloads).execute()

        if not answer_response.data:
            raise HTTPException(status_code=400, detail="Failed to insert answers")



        return JSONResponse(
            status_code=200,
            content={"message": "Question and answers created successfully"},
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating question: {str(e)}")
