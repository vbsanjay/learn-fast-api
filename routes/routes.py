from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from models import model
from schema import schema
from fastapi import APIRouter
from config.db import get_db

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)

@router.get('/', response_model=List[schema.CreateBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    post = db.query(model.Blog).all()
    return  post

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schema.CreateBlog])
def create_blog(post_post:schema.CreateBlog, db:Session = Depends(get_db)):
    """"""
    new_blog = model.Blog(**post_post.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return [new_blog]


@router.get('/{id}', response_model=schema.CreateBlog, status_code=status.HTTP_200_OK)
def get_one_blog(id:int ,db:Session = Depends(get_db)):
    """Await docstring generation..."""
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return blog

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db:Session = Depends(get_db)):
    deleted_blog = db.query(model.Blog).filter(model.Blog.id == id)
    if deleted_blog.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    deleted_blog.delete(synchronize_session=False)
    db.commit()

@router.put('/blogs/{id}', response_model=schema.CreateBlog)
def update_blog(put_put:schema.BlogBase, id:int, db:Session = Depends(get_db)):
    updated_blog =  db.query(model.Blog).filter(model.Blog.id == id)
    if updated_blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    updated_blog.update(put_put.dict(), synchronize_session=False)
    db.commit()
    return  updated_blog.first()