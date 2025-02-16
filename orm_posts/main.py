from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal
from schema import PostBase
from fastapi import HTTPException, status

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.get("/posts")
def delete_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {
        "message": posts
    }
    

# api to add a new post to the database 
@app.post("/post")
async def add_post(post: PostBase, db: Session = Depends(get_db)): 
    new_post = models.Post(title=post.title, content=post.content, published=post.published)
    db.add(new_post)
    db.commit()

    return {
        "message": "new post added successfully", 
        "post": post 
    }


@app.delete("/post/{id}")
async def delete_post(id: int, db: Session = Depends(get_db)): 
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {"message": "post has been deleted successfully"}


# api to updata a post
@app.put("/post/{id}")
async def update_post(id: int, post: PostBase, db: Session = Depends(get_db)): 
    query_post = db.query(models.Post).filter(models.Post.id == id)

    if query_post.first() == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    query_post.update(post.dict())
    db.commit()
    return {
        "message": "post successfully updated", 
        "post": query_post.first()
    }

