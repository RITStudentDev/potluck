from fastapi import FastAPI, HTTPException, Request,status
from models import Base, engine
import queries

"""
This file contains all of the FastAPI backend routes.
Each route is a point that the front end can direct a message to calling an
function from to perform an SQL query on the database. The data returned is 
sent to the front end in a response.
"""

app = FastAPI(title="Project Food")
Base.metadata.create_all(engine)

@app.get("/post/")
async def get_post():
    post = queries.get_post()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")
    return post

@app.get("/post/card")
async def get_post():
    post = queries.get_post_card()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")
    return post

@app.get("/user/{user_id}")
def get_user(user_id: int):
    user = queries.get_user(user_id)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return user