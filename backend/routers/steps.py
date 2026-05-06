from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2

router = APIRouter(
    prefix = "/steps",
    tags = ["Steps"]
)

@router.post("/add-steps")
def add_steps(steps: schemas.userSteps, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    user_steps = db.query(models.stepsHistory).filter()