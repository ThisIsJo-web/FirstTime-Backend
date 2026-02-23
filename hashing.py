from passlib.context import CryptContext             #IMPORTING THE CRYPTCONTEXT CLASS FROM PASSLIB, THIS WILL BE USED FOR PASSWORD HASHING

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class Hash():
    @staticmethod
    def hash(password: str):
        return pwd_context.hash(password)
    
    @staticmethod
    def verify(plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)
        