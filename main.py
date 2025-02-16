from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
async def root(): 
    return {"message": "Hello Happy New Year!"}


# Create an api for sending a post
class Post(BaseModel): 
    title: str
    content: str

@app.post("/post")
def create_post(new_post: Post): 
    print(new_post)
    return {"message": "Post created successfully"}