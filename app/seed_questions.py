from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Question, Answer

# Your data
questions_data = {
    "questions": [
  
        {
            "id": 1,
            "question_text": "What's your main goal?",
            "question_type": "single_mcq",
            "answers": [
                {"id": 1, "answer_text": "Lose weight", "subheading": None},
                {"id": 2, "answer_text": "Maintain weight", "subheading": None},
                {"id": 3, "answer_text": "Gain weight", "subheading": None},
                {"id": 4, "answer_text": "Build muscle", "subheading": None},
                {"id": 5, "answer_text": "Something else", "subheading": None}
            ],
            "subheading": None
        },
        {
            "id": 2,
            "question_text": "What would you like to accomplish?",
            "question_type": "multiple_mcq",
            "answers": [
                {"id": 6, "answer_text": "Eat & live healthier", "subheading": None},
                {"id": 7, "answer_text": "Boost my energy & mood", "subheading": None},
                {"id": 8, "answer_text": "Stay motivated & consistent", "subheading": None},
                {"id": 9, "answer_text": "Feel better about my body", "subheading": None},
                {"id": 10, "answer_text": "Strengthen my immune system", "subheading": None}
            ],
            "subheading": None
        },
        {
            "id": 3,
            "question_text": "Cal AI creates long-term results",
            "question_type": "image",
            "answers": [],
            "subheading": None
        },
        {
            "id": 4,
            "question_text": "Have you tried calorie counting before?",
            "question_type": "single_mcq",
            "answers": [
                {"id": 15, "answer_text": "I'm new to calorie counting", "subheading": None},
                {"id": 16, "answer_text": "I've tried it before but quit", "subheading": None},
                {"id": 17, "answer_text": "I'm Currently counting", "subheading": None}
            ],
            "subheading": None
        },
        {
            "id": 5,
            "question_text": "The ONLY Food Tracker That Actually Cares About Your Health, Not Just Weight",
            "question_type": "image",
            "answers": [],
            "subheading": None
        },
        {
            "id": 6,
            "question_text": "What type of diet do your prefer?",
            "question_type": "single_mcq",
            "answers": [
                {"id": 18, "answer_text": "Balanced", "subheading": None},
                {"id": 19, "answer_text": "Vegetarien", "subheading": None},
                {"id": 20, "answer_text": "Vegan", "subheading": None},
                {"id": 21, "answer_text": "Paleo", "subheading": None},
                {"id": 22, "answer_text": "Ketogenic", "subheading": None},
                {"id": 23, "answer_text": "High protein", "subheading": None},
                {"id": 24, "answer_text": "Low protein", "subheading": None}
            ],
            "subheading": None
        },
        {
            "id": 7,
            "question_text": "Choose products you don't eat.",
            "question_type": "multiple_mcq",
            "answers": [
                {"id": 25, "answer_text": "All meat", "subheading": None},
                {"id": 26, "answer_text": "Animal products", "subheading": None},
                {"id": 27, "answer_text": "Citrus fruits", "subheading": None},
                {"id": 28, "answer_text": "Dairy", "subheading": None},
                {"id": 29, "answer_text": "Nuts", "subheading": None},
                {"id": 30, "answer_text": "Fish", "subheading": None},
                {"id": 31, "answer_text": "Eggs", "subheading": None},
                {"id": 32, "answer_text": "Red meat", "subheading": None},
                {"id": 33, "answer_text": "Sea food", "subheading": None},
                {"id": 34, "answer_text": "Seeds", "subheading": None}
            ],
            "subheading": None
        },
        {
            "id": 8,
            "question_text": "What would you like to change in your eating habits?",
            "question_type": "multiple_mcq",
            "answers": [
                {"id": 35, "answer_text": "Reduce sugar intake", "subheading": None},
                {"id": 36, "answer_text": "Eat less junk food", "subheading": None},
                {"id": 37, "answer_text": "Stop binge eating", "subheading": None},
                {"id": 38, "answer_text": "Eat more greens & vegies", "subheading": None},
                {"id": 39, "answer_text": "Stop stress overeating", "subheading": None},
                {"id": 40, "answer_text": "Cook at home often", "subheading": None},
                {"id": 41, "answer_text": "Reduce sait intake", "subheading": None}
            ],
            "subheading": None
        },
        {
            "id": 9,
            "question_text": "What health goals would you like support with?",
            "question_type": "multiple_mcq",
            "answers": [
                {"id": 42, "answer_text": "Manage blood sugar levels", "subheading": None},
                {"id": 43, "answer_text": "Reduce inflammation", "subheading": None},
                {"id": 44, "answer_text": "Support heart health", "subheading": None},
                {"id": 45, "answer_text": "Track specific nutrients", "subheading": None},
                {"id": 46, "answer_text": "Identify food triggers", "subheading": None},
                {"id": 47, "answer_text": "Improve Digestive Issues", "subheading": None},
                {"id": 48, "answer_text": "Maintain energy levels", "subheading": None},
                {"id": 49, "answer_text": "Support brain health", "subheading": None},
                {"id": 50, "answer_text": "Boost my mood", "subheading": None}
            ],
            "subheading": None
        },
        {
            "id": 10,
            "question_text": "Guiding you with care",
            "question_type": "image-content",
            "answers": [],
            "subheading": "VitBite provides AI-powered nutrition insights for various health conditions-not just weight management. Our analysis covers inflammation, heart health, blood sugar, and specific nutrients for chronic conditions. However, our app is not a substitute for professional medical advice.\n\nBefore modifying your diet to address health concerns, always consult a qualified healthcare professional. Your personalized nutrition journey should complement your medical care plan."
        },
        {
            "id": 11,
            "question_text": "Choose you gender",
            "question_type": "single_mcq",
            "answers": [
                {"id": 51, "answer_text": "Male", "subheading": None},
                {"id": 52, "answer_text": "Female", "subheading": None},
                {"id": 53, "answer_text": "Others", "subheading": None}
            ],
            "subheading": None
        },
        {
            "id": 12,
            "question_text": "What is your age?",
            "question_type": "Age",
            "answers": [],
            "subheading": None
        },
        {
            "id": 13,
            "question_text": "How active are you?",
            "question_type": "single_mcq",
            "answers": [
                {"id": 54, "answer_text": "Lightly Active", "subheading": "Mostly sitting. e.g. office worker"},
                {"id": 55, "answer_text": "Moderately active", "subheading": "Mostly standing. e.g. teacher"},
                {"id": 56, "answer_text": "Active", "subheading": "Mostly walking. e.g. salesperson"},
                {"id": 57, "answer_text": "Very Active", "subheading": "Physically demanding. e.g. builder"}
            ],
            "subheading": "Knowing your daily activity level helps us calculate your calorie needs more accurately"
        },
        {
            "id": 14,
            "question_text": "Height & weight",
            "question_type": "height_weight",
            "answers": [],
            "subheading": "This will be used to calibrate your custom plan."
        },
        {
            "id": 15,
            "question_text": "What is your desired weight?",
            "question_type": "desired_weight",
            "answers": [],
            "subheading": None
        },
        {
            "id": 16,
            "question_text": "How fast do you want to reach your goal?",
            "question_type": "goal",
            "answers": [],
            "subheading": None
        },
        {
            "id": 17,
            "question_text": "Losing 5kg is a realistic target",
            "question_type": "image-celebration",
            "answers": [],
            "subheading": "You are just one step away from getting you personalized plan"
        },
        {
            "id": 18,
            "question_text": "Gain twice as much weight with VitBite vs on your own",
            "question_type": "image",
            "answers": [],
            "subheading": None
        },
        {
            "id": 19,
            "question_text": "What challenges did you face?",
            "question_type": "single_mcq",
            "answers": [
                {"id": 58, "answer_text": "Repleneshing burned calories.", "subheading": None},
                {"id": 59, "answer_text": "Staying motivated", "subheading": None},
                {"id": 60, "answer_text": "Eating enough quality foods", "subheading": None},
                {"id": 61, "answer_text": "Knowing what to eat", "subheading": None},
                {"id": 62, "answer_text": "Being too busy", "subheading": None},
                {"id": 63, "answer_text": "Something else", "subheading": None}
            ],
            "subheading": None
        },
        {
            "id": 20,
            "question_text": "Gain twice as much weight with VitBite vs on your own",
            "question_type": "image",
            "answers": [],
            "subheading": None
        },
        {
            "id": 21,
            "question_text": "You'll see positive effects on your health & well-being in no time. You can look forward to:",
            "question_type": "health_benefits",
            "answers": [
                {"id": 64, "answer_text": "Stronger immune system", "subheading": None},
                {"id": 65, "answer_text": "Improved energy levels", "subheading": None},
                {"id": 66, "answer_text": "Reduced stress", "subheading": None}
            ],
            "subheading": None
        }
    ]
}

    

def seed_database():
    db: Session = SessionLocal()
    
    try:
        # 🚫 Clear existing records
        db.query(Answer).delete()
        db.query(Question).delete()
        db.commit()

        # ✅ Insert new data
        for q in questions_data["questions"]:
            question = Question(
                id=q["id"],
                question_text=q["question_text"],
                question_type=q["question_type"],
                subheading=q.get("subheading")
            )
            db.add(question)

            for ans in q.get("answers", []):
                answer = Answer(
                    id=ans["id"],
                    question_id=q["id"],
                    answer_text=ans["answer_text"],
                    subheading=ans.get("subheading")
                )
                db.add(answer)

        db.commit()
        print("✅ Database seeded successfully!")

    except Exception as e:
        db.rollback()
        print("❌ Error seeding the database:", str(e))

    finally:
        db.close()

if __name__ == "__main__":
    seed_database()