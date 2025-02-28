from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int

    class Config:
        orm_mode = True

    
class UserCreate(BaseModel): 
    email: EmailStr
    password: str

class UserOut(BaseModel): 
    email: EmailStr

class UserLogin(BaseModel): 
    email: EmailStr
    password: str