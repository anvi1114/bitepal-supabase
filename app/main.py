from fastapi import FastAPI

# ✅ Updated imports based on your structure
from app.auth.signup import router as signup_router
from app.auth import login
from app.auth import questions
from app.database import Base, engine  # ← database.py is directly under app/
from app.routers import onboarding
from app.bmi.routes import router as bmi_router
from app.routers import review

# ✅ Create tables from SQLAlchemy models
#Base.metadata.create_all(bind=engine)

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Include all your routers
app.include_router(signup_router)
app.include_router(login.router)
app.include_router(questions.router)
app.include_router(onboarding.router)
app.include_router(bmi_router)
app.include_router(review.router)