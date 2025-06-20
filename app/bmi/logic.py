from datetime import datetime, timedelta
from app.models.onboarding import UserAnswer

def fetch_bmi_goal_info(user_id: int, db):
    answers = db.query(UserAnswer).filter_by(user_id=user_id).all()
    answer_dict = {ua.question_id: ua for ua in answers}

    # Required Question IDs — update if different
    HEIGHT_QID = 14
    GOAL_WEIGHT_QID = 15
    SPEED_QID = 16  # speed to reach goal

    height_ans = answer_dict.get(HEIGHT_QID)
    goal_weight_ans = answer_dict.get(GOAL_WEIGHT_QID)
    speed_ans = answer_dict.get(SPEED_QID)

    if not all([height_ans, goal_weight_ans, speed_ans]):
        raise Exception("Missing required onboarding data.")

    current_weight = height_ans.numeric_value  # assume weight stored here
    goal_weight = goal_weight_ans.numeric_value
    weeks = float(speed_ans.numeric_value or 8)

    reach_goal_by = datetime.today() + timedelta(weeks=weeks)

    return {
        "current_weight": current_weight,
        "goal_weight": goal_weight,
        "result_in_weeks": weeks,
        "reach_goal_by": reach_goal_by.strftime("%Y-%m-%d")
    }
