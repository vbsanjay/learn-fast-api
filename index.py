from fastapi import FastAPI, Header
from models import model as blog_model
from config.db import engine
from routes import routes as blog_router


# ito create table inside the db. kinda migration in django
blog_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# writing a simple endpoint in fast api
@app.get("/")
def hello_world():
    """Await docstring generation..."""
    return {"message":"hello world"}

@app.get("/hello")
def say_hello(name:str):
    """Await docstring generation..."""
    return {"message": f"hello, {name}"}

@app.get('/get_header')
def gert_header(accept: str = Header(None)):
    request_header = {}
    request_header["Accept"] = accept
    return request_header

app.include_router(blog_router.router)
