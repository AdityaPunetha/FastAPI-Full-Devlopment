from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import post, user, auth, vote


# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


# uvicorn app.main:app --reload
