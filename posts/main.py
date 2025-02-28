import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from schema import Post
from . import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)

def get_db(): 
    db = SessionLocal()

    try: 
        yield db 
    finally: 
        db.close()


app = FastAPI()



def get_database_conn(): 

    try: 
        conn = psycopg2.connect(
            host="localhost", 
            database="fastapi", 
            user="postgres", 
            password="mysimplelife", 
            cursor_factory=RealDictCursor
        )

        return conn
    except Exception as e: 
        print("Failed to connect to database")
        print("Error: ", e)

# Now let's start making api calls 
@app.get("/posts")
async def get_posts(): 
    conn = get_database_conn()
    cursor = conn.cursor()
    try: 
        cursor.execute(
            """
            SELECT * FROM posts;
        """
        )

        posts = cursor.fetchall()
        return {
            "message": "fetch successfull!", 
            "posts": posts
        }
    
    finally: 
        cursor.close()
        conn.close()


# Let's make an api call to add data to the database 
@app.post("/post")
async def create_post(post: Post): 
    conn = get_database_conn()
    cursor = conn.cursor()

    try: 
        cursor.execute(
            """
                INSERT INTO posts (title, content, published)
                VALUES (%s, %s, %s) RETURNING *;
            """, 
            (post.title, post.content, post.published)
        )
        post = cursor.fetchone()
        conn.commit()
        return {
            "message": "Post made successfully", 
            "post": post
        }
    finally: 
        cursor.close()
        conn.close()



@app.get("/posts/{id}")
async def get_by_id(id: int): 
    conn = get_database_conn()
    cursor = conn.cursor()

    try: 
        cursor.execute(
            """
            SELECT * FROM posts
            WHERE id = %s
            """, 
            (id, )
        )

        post = cursor.fetchone()
        # if post is None: 
        #     raise HTTPException(status_code=404, detail="Post Not Found!")
        return {"message": "Successful", "post": post}
       
    finally: 
        cursor.close()
        conn.close()

# api for making updates 
@app.put("/posts/{id}")
async def update_post(id: int, updated_post): 
    conn = get_database_conn()
    cursor = conn.cursor()
    try: 
        cursor.execute(
            """
            UPDATE posts
            SET title = %s content = %s
            WHERE id = %s
            RETURNING *
            """, 
            (updated_post.title, updated_post.content, id)
        )

        post = cursor.fetchone()
        return {"message":"updated post successfully", "post": post}
    finally: 
        cursor.close()
        conn.close()


# testing the sql alchemy 
@app.get("/sqlachemy")
def test_results(db: Session = Depends(get_db)): 
    return {"message": "It was a success"}