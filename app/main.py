from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from app import models
from app.database import engine
from app.routers import post, user, auth

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
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


# uvicorn app.main:app --reload
