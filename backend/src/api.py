from fastapi import FastAPI, HTTPException, Request, status
from sqlalchemy.exc import IntegrityError
from fastapi.concurrency import run_in_threadpool
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

@app.post("/post/", status_code=status.HTTP_201_CREATED)
async def create_post(request: Request):
    try:
        body = await request.json()
    except ValueError:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid JSON")

    owner = body.get("owner")
    url = body.get("url")
    description = body.get("description")
    if not isinstance(owner, int) or isinstance(owner, bool):
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "Owner must be an int")
    if not isinstance(url, str) or not url.strip():
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "URL is required")
    if not isinstance(description, str) or not description.strip():
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, "Description is required")

    user = await run_in_threadpool(queries.get_user, owner)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Owner not found")
    return await run_in_threadpool(queries.create_post, owner, url.strip(), description.strip())


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

@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(request: Request):
    try:
        body = await request.json()
    except ValueError:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Invalid JSON")

    uname = body.get("username")
    pword = body.get("password")
    lang = body.get("language", "English")

    if not isinstance(uname, str) or not isinstance(pword, str) or not uname or not pword:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Username and password are required")

    try: 
        return queries.enter_user(uname, pword, lang)
    except IntegrityError:
        raise HTTPException(status.HTTP_409_CONFLICT, "User data conflict")

@app.get("/user/{user_id}")
def get_user(user_id: int):
    user = queries.get_user(user_id)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return user