import database
from sqlalchemy.orm import Session
from models import engine, Post, PostImages, User
from sqlalchemy import insert, select, desc
import hashlib

"""
This file contains functions for SQL queries using SQL Alchemy.
These functions are called in api.py to handle api logic.
"""

def to_dict(row):
    return dict(row._mapping) if row is not None else None

def create_post(owner: int, url: str, description: str):
    with Session(engine) as session:
        post = session.execute(
            insert(Post).values(owner=owner, description=description)
        )
        post_id = post.inserted_primary_key[0]

        session.execute(
            insert(PostImages).values(post_id=post_id, image_url=url)
        )
        session.commit()

        record = session.execute(
            select(
                Post.id,
                Post.owner,
                Post.like_num,
                Post.description,
                Post.post_time,
                PostImages.image_url
            ).join(PostImages, PostImages.post_id == Post.id)
            .where(Post.id == post_id)
        ).first()
        return to_dict(record)

def get_post():
    with Session(engine) as session:
        post = session.execute(
            select(
                Post.like_num,
                Post.owner,
                Post.description,
                Post.post_time
            ).order_by(desc(Post.like_num))
        ).first()

        return to_dict(post)

def get_post_card():
    with Session(engine) as session:
        post = session.execute(
            select(
                User.username,
                Post.like_num,
                PostImages.image_url,
                Post.id
            ).join(PostImages, PostImages.post_id == Post.id).join(User, User.id == Post.owner).order_by(Post.like_num)
        ).first()

        return to_dict(post)
    
def get_user(user_id: int):
    with Session(engine) as session:
        user = session.execute(
            select(
                User.id,
                User.username,
                User.language
            ).where(User.id == user_id)
        ).first()

        return to_dict(user)

def enter_user(username: str, password: str, language: str):
    with Session(engine) as session:
        user = session.execute(
            insert(User).values(
                username=username,
                password=hashlib.sha256(password.encode()).hexdigest(),
                language=language
            )
        )
        session.commit()
        user_id = user.inserted_primary_key[0]

        return get_user(user_id)
    
