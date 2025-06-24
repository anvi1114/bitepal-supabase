# BitePal Supabase Backend

BitePal is an AI-powered nutrition tracking platform designed to help users manage their health through personalized diet and lifestyle guidance. This repository contains the backend codebase developed using FastAPI, SQLAlchemy, and PostgreSQL (Supabase).

## Project Overview

The backend handles core functionalities such as user onboarding, BMI and goal-related calculations, review submissions, and food recognition R&D integration. It is structured to be scalable, modular, and adaptable to evolving health-tech features.

## Tech Stack

- FastAPI (Python 3.11+)
- PostgreSQL (via Supabase)
- SQLAlchemy ORM
- Pydantic for request validation
- Alembic for migrations (optional)
- Nutrition APIs (Edamam, Spoonacular)
- Image classification (R&D with YOLOv5, CNNs)

## Implemented Features

### User Onboarding

- Dynamic question-answer system
- Multiple question types supported (MCQ, input, image-based)
- Stores both metric and imperial values for height and weight
- Captures target goals and preferences

### BMI and Goal Info

- Calculates BMI and returns:
  - Current weight
  - Target weight
  - Timeframe to reach the goal
  - Estimated goal date
- Considers unit type (kg/lb)

### User Reviews

- Submit a review with username, content, and rating
- Retrieve all reviews submitted across the platform
- Get average rating and total number of reviews

## Work in Progress

### AI-Based Food Recognition (Research Phase)

- Users will upload images of food
- Food items and ingredients will be detected using image classification
- Nutrition data will be fetched via APIs or custom datasets

Resources being explored:
- Indian Food Image Dataset
- Food-101
- YOLOv5 for detection
- Edamam and Spoonacular APIs

## Project Structure

bitepal-supabase/
│
├── app/
│ ├── auth/
│ ├── models/
│ ├── schemas/
│ ├── routers/
│ ├── database.py
│ └── main.py
│
├── .env
├── requirements.txt
└── README.md

markdown
Copy code

## Setup Instructions

1. Clone the repository:
git clone https://github.com/anvi1114/bitepal-supabase.git
cd bitepal-supabase

markdown
Copy code

2. Install dependencies:
pip install -r requirements.txt

markdown
Copy code

3. Set environment variables in `.env` file

4. Run the server:
uvicorn app.main:app --reload

markdown
Copy code

## Challenges Faced

- Designing a flexible onboarding system to handle dynamic question types
- Managing dual unit systems for accurate goal tracking
- Aligning backend APIs with Figma-based frontend expectations
- Finding reliable nutrition data sources for Indian food
- Planning an efficient image-to-nutrition flow using AI

## Contributors

- Backend Developer: Anvi Goyal
- Supported by: BitePal frontend & design team

## License

This project is proprietary and currently under development. Usage rights reserved by the BitePal team.