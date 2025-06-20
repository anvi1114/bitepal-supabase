from pydantic import BaseModel, EmailStr

class SignupRequest(BaseModel):
    fullname: str
    email: EmailStr
    password: str
    deviceId: str
    deviceType: str
