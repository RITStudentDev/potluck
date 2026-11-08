from fastapi import APIRouter, HTTPException, Request, status, Query
from sqlalchemy.exc import IntegrityError
from fastapi.concurrency import run_in_threadpool
from translate import translate_text
from . import queries

"""
This file contains all of the FastAPI backend routes.
Each route is a point that the front end can direct a message to calling an
function from to perform an SQL query on the database. The data returned is 
sent to the front end in a response.
"""

router = APIRouter()

@router.post("/post/", status_code=status.HTTP_201_CREATED)
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

@router.post("/post/{post_id}/like", status_code=status.HTTP_204_NO_CONTENT)
async def like_post(post_id: int):
    success = await run_in_threadpool(queries.like_post, post_id)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@router.get("/post/")
async def get_post():
    post = queries.get_post()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")
    return post

@router.get("/post/{post_id}/translation")
def get_post_translation(post_id: int, lang: str = Query(..., min_length=2, max_length=10)):
    post = queries.get_post_by_id(post_id, lang)
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")

    lang = lang.lower()
    source = post["owner_language"]
    if source == lang:
        return {"language": lang, "description": post["description"], "instructions": post["instructions"], "translated": False}

    cached = queries.get_translation(post_id, lang)
    if cached is not None:
        return {"language": lang, "description": cached, "instructions": cached, "translated": True}
    

    try:
        translated_dec = translate_text(post["description"], source, lang)
        translated_ins = translate_text(post["instructions"], source, lang)
    except Exception:
        raise HTTPException(status.HTTP_502_BAD_GATEWAY, "Translation failed")

    queries.save_translation(post_id, lang, translated_dec, translated_ins)
    return {"language": lang, "description": translated_dec, "instructions": translated_ins, "translated": True}

@router.get("/posts/")
def get_all_posts(limit: int = Query(50, ge=1, lt=100), offset: int = Query(0, ge=0)):
    return queries.get_all_posts(limit, offset)

@router.get("/post/card")
async def get_post():
    post = queries.get_post_card()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")
    return post

@router.post("/user/", status_code=status.HTTP_201_CREATED)
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

@router.get("/user/{user_id}")
def get_user(user_id: int):
    user = queries.get_user(user_id)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return user