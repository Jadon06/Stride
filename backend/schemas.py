from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class userCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
    goal_steps: Optional[int] = 5000

class userUpdate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
    goal_steps: Optional[int] = 5000

class userReturn(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
    goal_steps: Optional[int] = 5000
    
    class Config:
        orm_mode = True

class userSteps(BaseModel):
    step_count_daily: int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
