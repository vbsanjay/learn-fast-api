# is used to define the structure of data you except in request and response

from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    content: str

    class Config: #class used to configure behavior of pydantic model
        orm_mode = True #tells pydantic to treat the data like it's coming from an orm

class CreateBlog(BlogBase):
    class Config:
        orm_mode = True
