from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def validate_password(password: str):
    special_chars = "!@#$%&"
    capital_letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    allowed = special_chars + capital_letters + lower_case_letters + numbers
    special_chars = 0
    caps = 0
    nums = 0
    length = len(password)
    for letter in password:
        if letter in special_chars:
            special_chars += 1
        if letter in capital_letters:
            caps += 1
        if letter in numbers:
            nums += 1
        if letter not in allowed:
            return False
    return special_chars >= 1 and caps >= 2 and numbers >= 3 and (10 <= length <= 20)


@router.post("/create", response_model=schemas.userReturn)
async def create_user(user: schemas.userCreate, db: Session = Depends(get_db)):
    user_exists = db.query(models.Users).filter(models.Users.email == user.email)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"user with email:{user.email} already exists")
    if not validate_password(user.password):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="""Password must contain the following:
                                                                                1 special character(!@#$%&), 2 capital letters 
                                                                                and 3 numbers with a minimum length of 10 and
                                                                                maximum length of 20""")

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put("/update", response_model=schemas.userReturn)
async def update_user(user_data: schemas.userUpdate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()
    password_change = utils.verify(user_data.password, user.password)
    if not password_change:
        user_data.password = utils.hash(user_data.password) 
    
    db.query(models.Users).filter(models.Users.id == user_id.id).update(user_data.dict())
    db.commit()
    db.refresh(user)
    return user

@router.delete("/delete")
def delete_user(db: Session = Depends(get_db), user: int = Depends(oauth2.get_current_user)):
    user = db.query(models.Users).filter(models.Users.id == user.id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return "deleted successfully"