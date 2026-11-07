import database
from sqlalchemy.orm import Session
from models import Post, PostImages, User
import hashlib

engine = database.engine
from sqlalchemy import insert, select, desc

def get_big_post():
    with Session(engine) as session:
        post = session.execute(
            select(
                Post.like_num,
                Post.owner,
                Post.description,
                Post.post_time
            ).order_by(desc(Post.like_num))
        ).first()

        return post

def get_little_post():
    with Session(engine) as session:
        post = session.execute(
            select(
                User.username,
                Post.like_num,
                PostImages.image_url,
                Post.id
            ).join(PostImages, PostImages.post_id == Post.id).join(User, User.id == Post.owner).order_by(Post.like_num)
        ).first()

        return post
    
def get_user(user_id: int):
    with Session(engine) as session:
        user = session.execute(
            select(
                User.id,
                User.username,
                User.language
            ).where(User.id == user_id)
        ).first()

        return user

def enter_user(username: str, password: str, language: str):
    with Session(engine) as session:
        user = session.execute(
            insert(User).values(
                username=username,
                password=hashlib.sha256(password.encode()).hexdigest(),
                language=language
            )
        ).first()

        return user
    
