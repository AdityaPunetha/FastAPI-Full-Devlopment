from fastapi import FastAPI, status, Response, HTTPException, Depends
from fastapi.params import Body
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


try:
    conn = psycopg2.connect(
        host="localhost",
        database="fastapi",
        user="postgres",
        password="root",
        cursor_factory=RealDictCursor,
    )
    cursor = conn.cursor()
    print("Connection to PostgreSQL DB successful")

except Exception as error:
    print("Error while connecting to PostgreSQL")
    print(error)


app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


# uvicorn app.main:app --reload
