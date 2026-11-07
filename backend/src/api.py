from fastapi import FastAPI, HTTPException, status
import models

app = FastAPI(title="Project Food")

@app.get("/post/", response_model=models.Post)
async def get_post():
    post = 123
    return  post