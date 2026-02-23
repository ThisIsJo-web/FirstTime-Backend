from fastapi import HTTPException
from sqlalchemy.orm import Session
import schemas
from database import get_db
import models

def get_all(db: Session):
    blogs = db.query(models.Blog).all()                                 #QUERYING THE DATABASE FOR ALL BLOGS, THIS RETURNS A LIST OF ALL BLOG INSTANCES IN THE DATABASE
    return blogs                                                        #RETURNING THE LIST OF BLOGS AS THE RESPONSE TO THE API CALL, THIS WILL BE AUTOMATICALLY CONVERTED TO JSON BY FASTAPI

def get_by_id(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()    #QUERYING THE DATABASE FOR A BLOG WITH A SPECIFIC ID, THIS RETURNS THE FIRST BLOG INSTANCE THAT MATCHES THE ID OR NONE IF NOT FOUND
    if not blog:                                                              #CHECKING IF THE BLOG WAS NOT FOUND, IF NOT FOUND, RAISE AN HTTP EXCEPTION WITH A 404 STATUS CODE
        raise HTTPException(status_code=404, detail="Blog not found")         #RAISING AN HTTP EXCEPTION WITH A 404 STATUS CODE AND A DETAIL MESSAGE INDICATING THAT THE BLOG WAS NOT FOUND
    
    return blog                                                               #RETURNING THE BLOG INSTANCE AS THE RESPONSE TO THE API CALL, THIS WILL BE AUTOMATICALLY CONVERTED TO JSON BY FASTAPI

def create(db: Session, blog: schemas.Blog):
    new_blog = models.Blog(title=blog.title, content=blog.content, user_id=1)      #CREATING A NEW INSTANCE OF THE MODELS.BLOG CLASS, USING THE DATA FROM THE INPUT BLOG OBJECT
    db.add(new_blog)                                                    #ADDING THE NEW BLOG INSTANCE TO THE DATABASE SESSION, THIS MARKS IT FOR INSERTION INTO THE DATABASE
    db.commit()                                                         #COMMITTING THE TRANSACTION TO THE DATABASE, THIS ACTUALLY PERFORMS THE INSERTION OF THE NEW BLOG INTO THE DATABASE
    db.refresh(new_blog)                                                #REFRESHING THE NEW BLOG INSTANCE TO GET THE UPDATED DATA FROM THE DATABASE, THIS IS USEFUL TO GET THE ID OF THE NEW BLOG AFTER IT HAS BEEN INSERTED
    return new_blog                                                     #RETURNING THE NEW BLOG INSTANCE AS THE RESPONSE TO THE API CALL, THIS WILL BE AUTOMATICALLY CONVERTED TO JSON BY FASTAPI

def delete(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)  
    db.commit()
    return{'done': True}

def update(db: Session, id: int, request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"Blog with id {id} not found")
    blog.update({'title': request.title, 'content': request.content}, synchronize_session=False)
    db.commit()
    return {'updated': True}