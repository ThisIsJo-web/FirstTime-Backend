from fastapi import HTTPException  #FASTAPI FOR CREATING THE API, DEPENDS FOR DEPENDENCY INJECTION, HTTPException FOR HANDLING ERRORS
import models
from database import get_db 
from sqlalchemy.orm import Session                   #IMPORTING THE SESSION CLASS FROM SQLALCHEMY ORM
from hashing import Hash                          #IMPORTING THE HASH CLASS FROM THE HASHING MODULE FOR PASSWORD HASHING


def get_user_id(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user

def create_user(db: Session, request: models.User):
    new_user = models.User(name=request.name, password=Hash.hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'message': f'User {new_user.name} created successfully with hashed password'}