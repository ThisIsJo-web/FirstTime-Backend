from pydantic import BaseModel  #IMPORTING THE BASEMODEL CLASS FROM PYDANTIC, 
                                #THIS IS THE BASE CLASS FOR ALL OUR SCHEMAS, 
                                #THIS WILL BE USED TO DEFINE THE STRUCTURE OF OUR REQUEST BODIES AND RESPONSE MODELS

#REQUEST BODY|| Pydantic Model/Schema
class Blog(BaseModel):
    title: str
    content: str

class User(BaseModel):
    name: str
    password: str

class showUser(BaseModel):
    name: str
    blogs: list[Blog] = [] #THIS DEFINES A FIELD FOR THE USER SCHEMA THAT IS A LIST OF BLOGS, THIS ALLOWS US TO INCLUDE THE BLOGS CREATED BY THE USER IN THE RESPONSE WHEN WE GET A USER

    class Config:
        from_attributes = True

class showBlog(Blog):          #DEFINING A NEW SCHEMA FOR THE RESPONSE MODEL, THIS INHERITS FROM THE BLOG SCHEMA, THIS MEANS IT WILL HAVE ALL THE FIELDS OF THE BLOG SCHEMA PLUS ANY ADDITIONAL FIELDS WE DEFINE
    title: str
    content: str
    creator: showUser

    class Config:
        from_attributes = True #THIS CONFIGURATION OPTION ALLOWS US TO WORK WITH ORMS LIKE SQLALCHEMY, THIS MEANS WE CAN RETURN SQLALCHEMY MODELS DIRECTLY AND THEY WILL BE CONVERTED TO THE SCHEMA FORMAT AUTOMATICALLY

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
