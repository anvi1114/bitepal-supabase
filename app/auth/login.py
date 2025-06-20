from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models.login_schema import LoginRequest
from app.supabase_client import supabase

router = APIRouter()

@router.post("/authentication/login/")
def login_user(user: LoginRequest):
    try:
        print("Trying to log in...")  # TEMP
        response = supabase.auth.sign_in_with_password({
            "email": user.email.strip().lower(),
            "password": user.password
        })

        print("Login response:", response)  # TEMP

        if response.session is None or response.user is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if not response.user.confirmed_at:
            raise HTTPException(status_code=401, detail="Email not confirmed")

        supabase_uid = response.user.id

        profile_response = supabase.table("user_profiles").select("*").eq("supabaseUID", supabase_uid).execute()

        print("Profile response:", profile_response.data)  # TEMP

        if not profile_response.data:
            raise HTTPException(status_code=404, detail="User profile not found")

        user_profile = profile_response.data[0]

        return JSONResponse(content={
            "status": 200,
            "message": "Login successful",
            "data": {
                "user": {
                    "id": user_profile["id"],
                    "email": user_profile["email"],
                    "fullname": user_profile["fullname"],
                    "supabaseUID": supabase_uid
                },
                "loginType": "normal",
                "accessToken": response.session.access_token
            }
        })

    except HTTPException as http_err:
        print("HTTPException:", http_err.detail)
        raise http_err
    except Exception as e:
        print("Exception:", str(e))
        raise HTTPException(status_code=500, detail=f"Login error: {str(e)}")
