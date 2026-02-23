from fastapi import APIRouter, Depends  #FASTAPI FOR CREATING THE API, DEPENDS FOR DEPENDENCY INJECTION, HTTPException FOR HANDLING ERRORS
from database import get_db
import schemas
from sqlalchemy.orm import Session                   #IMPORTING THE SESSION CLASS FROM SQLALCHEMY ORM
from Repos import UserRepo

router = APIRouter(
    prefix="/user",
    tags=['User']
)

@router.get("/{user_id}", status_code=200, response_model=schemas.showUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserRepo.get_user_id(user_id, db)

@router.post("/", status_code=201)                            #DEFINING A POST ENDPOINT AT THE PATH /user, THIS ENDPOINT WILL BE USED TO CREATE A NEW USER, THE RESPONSE MODEL IS SET TO SCHEMAS.SHOWUSER TO SPECIFY THE STRUCTURE OF THE RESPONSE
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return UserRepo.create_user(db, request)                                              #CALLING THE create_user FUNCTION FROM THE User REPOSITORY TO CREATE A NEW USER IN THE DATABASE USING THE DATA FROM THE INPUT USER OBJECT, AND RETURNING THE RESULT AS THE RESPONSE TO THE API CALL, THIS WILL BE AUTOMATICALLY CONVERTED TO JSON BY FASTAPI

