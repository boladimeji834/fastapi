from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, utils
from database import engine
from router import posts, users  # Fixed import

models.Base.metadata.create_all(bind=engine)  # Remove this if using Alembic

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)


# Dependency for database session





# @app.get("/posts")
# def delete_post(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {
#         "message": posts
#     }
    

# # api to add a new post to the database 
# @app.post("/post")
# async def add_post(post: schemas.PostBase, db: Session = Depends(get_db)): 
#     new_post = models.Post(title=post.title, content=post.content, published=post.published)
#     db.add(new_post)
#     db.commit()

#     return {
#         "message": "new post added successfully", 
#         "post": post 
#     }


# @app.delete("/post/{id}")
# async def delete_post(id: int, db: Session = Depends(get_db)): 
#     post = db.query(models.Post).filter(models.Post.id == id)
#     if post.first() == None: 
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
#     post.delete(synchronize_session=False)
#     db.commit()
#     return {"message": "post has been deleted successfully"}


# # api to updata a post
# @app.put("/post/{id}")
# async def update_post(id: int, post: schemas.PostBase, db: Session = Depends(get_db)): 
#     query_post = db.query(models.Post).filter(models.Post.id == id)

#     if query_post.first() == None: 
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#     query_post.update(post.dict())
#     db.commit()
#     return {
#         "message": "post successfully updated", 
#         "post": query_post.first()
#     }

# # api to create a new user and add it to the database 
# @app.post("/user", status_code=200, response_model=schemas.UserOUt)
# async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)): 
#     hashed_pwd = hash(user.password)
#     user.password = hashed_pwd
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return user.dict()

