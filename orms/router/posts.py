from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db  # Use absolute import
import schemas, utils, models  # Use absolute imports

router = APIRouter()





@router.get("/posts")
def get_all_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {
        "message": posts
    }
    
@router.get("/post/{id}")
async def post_by_id(id: int, db: Session = Depends(get_db)): 
    post = db.query(models.Post).filter(models.Post.id == id).first()
    return post

# api to add a new post to the database 
@router.post("/post")
async def add_post(post: schemas.PostBase, db: Session = Depends(get_db)): 
    new_post = models.Post(title=post.title, content=post.content, published=post.published)
    db.add(new_post)
    db.commit()

    return {
        "message": "new post added successfully", 
        "post": post 
    }


@router.delete("/post/{id}")
async def delete_post(id: int, db: Session = Depends(get_db)): 
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {"message": "post has been deleted successfully"}


# api to updata a post
@router.put("/post/{id}")
async def update_post(id: int, post: schemas.PostBase, db: Session = Depends(get_db)): 
    query_post = db.query(models.Post).filter(models.Post.id == id)

    if query_post.first() == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    query_post.update(post.dict())
    db.commit()
    return {
        "message": "post successfully updated", 
        "post": query_post.first()
    }