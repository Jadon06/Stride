from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2

router = APIRouter(
    prefix = "/steps",
    tags = ["Steps"]
)

@router.post("/create-daily-step-count")
def start_step_count(user_id: int = Depends(oauth2.get_current_user), db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()
    new_step_count = models.stepsHistory(user_id=user_id, step_count_daily=0, goal_steps=user.goal_steps)
    db.add(new_step_count)
    db.commit()
    db.refresh(new_step_count)
    return new_step_count

@router.put("/add-steps")
def add_steps(steps: schemas.userSteps, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    step_count = db.query(models.stepsHistory).filter(models.stepsHistory.user_id == user_id).first()
    step_count.step_count_daily += steps.step_count_daily
    db.commit()
    db.refresh(step_count)
    return step_count