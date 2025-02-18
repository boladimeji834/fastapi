from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session 
from database import get_db
import models, utils, schemas


router = APIRouter()

@router.get("/login")
async def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)): 
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if user == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not utils.verify_password(user_credentials.password, user.password): 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    return {"message": "login successful"}