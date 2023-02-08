
from fastapi import FastAPI
from app.models.user import User
from fastapi_sqlalchemy import DBSessionMiddleware, db


app = FastAPI()

@app.get('/test')
async def test():
  query = db.session.query(User)
  return query.all()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}



