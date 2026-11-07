from fastapi import FastAPI, HTTPException, status
import models, queries

app = FastAPI(title="Project Food")

@app.get("/post/")
async def get_post():
    post = queries.get_big_post()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")
    return  post

@app.get("/user/{user_id}")
def get_user(user_id: int):
    user = queries.get_user(user_id)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return user