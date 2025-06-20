from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models.signup_schema import SignupRequest
from app.supabase_client import supabase            # import client

router = APIRouter()

@router.post("/authentication/signup/")
def signup_user(user: SignupRequest):
    try:
        response = supabase.auth.sign_up({
            "email": user.email.strip().lower(),
            "password": user.password
        })

        if response.user is None:
            raise HTTPException(status_code=400, detail="Signup failed.")

        supabase_uid = response.user.id

        # Insert into 'user_profiles' table
        profile_data = {
            "fullname": user.fullname,
            "email": user.email,
            "deviceId": user.deviceId,
            "deviceType": user.deviceType,
            "supabaseUID": supabase_uid
        }

        profile_response = supabase.table("user_profiles").insert(profile_data).execute()

        user_id = profile_response.data[0]['id']

        return JSONResponse(content={
            "status": 200,
            "message": "User registered successfully",
            "data": {
                "user": {
                    "id": user_id,
                    "email": user.email,
                    "fullname": user.fullname,
                    "supabaseUID": supabase_uid
                },
                "loginType": "normal",
                "accessToken": response.session.access_token if response.session else ""
            }
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Signup error: {str(e)}")
