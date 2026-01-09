from pydantic import BaseModel, EmailStr, field_validator


class RegisterUser(BaseModel):
    emp_id: str
    name: str
    email: EmailStr
    password: str
    confirm_password: str
    role: str

    @field_validator("email")
    @classmethod
    def email_must_be_aptivora(cls, v):
        if not v.endswith("@aptivora.it"):
            raise ValueError("Only @aptivora.it email allowed")
        return v

    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, v, info):
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("Passwords do not match")
        return v


class LoginUser(BaseModel):
    emp_id: str
    password: str

from pydantic import BaseModel
from datetime import date

class JobCreate(BaseModel):
    job_title: str
    job_description: str
    expected_close_date: date
    budget: float
    emp_id: str


class JobResponse(BaseModel):
    id: int
    job_title: str
    job_description: str
    expected_close_date: date
    budget: float
    emp_id: str

    class Config:
        from_attributes = True

