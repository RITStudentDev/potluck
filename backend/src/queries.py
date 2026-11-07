import database
from sqlalchemy.orm import Session
from models import Post

engine = database.engine
from sqlalchemy import select, desc

def get_big_post():
    with Session(engine) as session:
        post = session.execute(
            select(
                Post.likeNum,
                Post.owner,
                Post.description,
                Post.postTime
            ).order_by(desc(Post.likeNum))
        ).first()

        return post

def get_little_post():
    with Session(engine) as session:
        post = session.execute(
            select(
                Post.owner,
                Post.likeNum,
                
            ).order_by(Post.likeNum)
        ).first()

        return post