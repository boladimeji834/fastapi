from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db  # Use absolute import
import schemas, utils, models  # Use absolute imports

router = APIRouter()



router = APIRouter()




# api to create a new user and add it to the database 
@router.post("/user", status_code=200, response_model=schemas.UserOUt)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)): 
    hashed_pwd = hash(user.password)
    user.password = hashed_pwd
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return user.dict()