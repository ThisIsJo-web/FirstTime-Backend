from fastapi import APIRouter, Depends, HTTPException  #FASTAPI FOR CREATING THE API, DEPENDS FOR DEPENDENCY INJECTION, HTTPException FOR HANDLING ERRORS
import schemas, models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from Repos import BlogRepo
from oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get("/")                                                  #DEFINING A GET ENDPOINT AT THE PATH /get_blogs, THIS ENDPOINT WILL BE USED TO GET ALL BLOG POSTS
def get_blogs(db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(get_current_user)):                           #THE ENDPOINT FUNCTION TAKES A DATABASE SESSION AS INPUT, WHICH IS INJECTED USING THE DEPENDS FUNCTION AND THE get_db DEPENDENCY
    return BlogRepo.get_all(db)                                              #CALLING THE get_all FUNCTION FROM THE Blog REPOSITORY TO GET ALL BLOGS FROM THE DATABASE, AND RETURNING THE RESULT AS THE RESPONSE TO THE API CALL, THIS WILL BE AUTOMATICALLY CONVERTED TO JSON BY FASTAPI

@router.get("/{blog_id}",status_code=200, response_model=schemas.showBlog, ) #DEFINING A GET ENDPOINT AT THE PATH /get_blog/{blog_id}, THIS ENDPOINT WILL BE USED TO GET A SINGLE BLOG POST BY ID, THE RESPONSE MODEL IS SET TO SCHEMAS.SHOWBLOG TO SPECIFY THE STRUCTURE OF THE RESPONSE
def get_blog_id(blog_id: int, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(get_current_user)):                           #THE ENDPOINT FUNCTION TAKES A BLOG ID AS A PATH PARAMETER, A DATABASE SESSION AS INPUT, WHICH IS INJECTED USING THE DEPENDS FUNCTION AND THE get_db DEPENDENCY
    return BlogRepo.get_by_id(db, blog_id)                                              #CALLING THE get_by_id FUNCTION FROM THE Blog REPOSITORY TO GET A SINGLE BLOG BY ID FROM THE DATABASE, AND RETURNING THE RESULT AS THE RESPONSE TO THE API CALL, THIS WILL BE AUTOMATICALLY CONVERTED TO JSON BY FASTAPI


#Create Blog Post
@router.post("/", status_code=201)                                               #DEFINING A POST ENDPOINT AT THE PATH /create_blog, THIS ENDPOINT WILL BE USED TO CREATE A NEW BLOG POST
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(get_current_user)):     #THE ENDPOINT FUNCTION TAKES A BLOG OBJECT AS INPUT, WHICH IS VALIDATED AGAINST THE SCHEMAS.BLOG MODEL, AND A DATABASE SESSION WHICH IS INJECTED USING THE DEPENDS FUNCTION AND THE get_db DEPENDENCY
    return BlogRepo.create(db, blog)                                              #CALLING THE create FUNCTION FROM THE Blog REPOSITORY TO CREATE A NEW BLOG IN THE DATABASE USING THE DATA FROM THE INPUT BLOG OBJECT, AND RETURNING THE RESULT AS THE RESPONSE TO THE API CALL, THIS WILL BE AUTOMATICALLY CONVERTED TO JSON BY FASTAPI

@router.delete("/{id}")                                              #DEFINING A DELETE ENDPOINT AT THE PATH /delete_blog/{id}, THIS ENDPOINT WILL BE USED TO DELETE A BLOG POST BY ID, THE RESPONSE MODEL IS SET TO SCHEMAS.SHOWBLOG TO SPECIFY THE STRUCTURE OF THE RESPONSE
def delete_blog(id, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(get_current_user)):
    return BlogRepo.delete(db, id)                                              #CALLING THE delete FUNCTION FROM THE Blog REPOSITORY TO DELETE A BLOG BY ID FROM THE DATABASE, AND RETURNING THE RESULT AS THE RESPONSE TO THE API CALL, THIS WILL BE AUTOMATICALLY CONVERTED TO JSON BY FASTAPI


@router.put('/{id}', status_code=202)                                              #DEFINING A PUT ENDPOINT AT THE PATH /update_blog/{id}, THIS ENDPOINT WILL BE USED TO UPDATE A BLOG POST BY ID, THE RESPONSE MODEL IS SET TO SCHEMAS.SHOWBLOG TO SPECIFY THE STRUCTURE OF THE RESPONSE
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(get_current_user)):
    return BlogRepo.update(db, id, request)                                              #CALLING THE update FUNCTION FROM THE Blog REPOSITORY TO UPDATE A BLOG BY ID IN THE DATABASE USING THE DATA FROM THE INPUT BLOG OBJECT, AND RETURNING THE RESULT AS THE RESPONSE TO THE API CALL, THIS WILL BE AUTOMATICALLY CONVERTED TO JSON BY FASTAPI
