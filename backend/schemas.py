from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class userCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str = Field(..., min_length=10, max_length=20)
    phone_number: Optional[str] = None
    

class userUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str = Field(..., min_length=10, max_length=20)
    phone_number: Optional[str] = None

class userReturn(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str = Field(..., min_length=10, max_length=20)
    phone_number: Optional[str] = None
    
    class Config:
        orm_mode = True

class userSteps(BaseModel):
    step_count_daily: int
    goal_steps: Optional[int] = 5000