from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.models.user import User
from db.session import get_db
from repositories.blog import BlogRepository
from repositories.user import UserRepository
from schema.blog import BlogCreate, BlogPagination, BlogRead, BlogSingleRead, BlogUpdate

router = APIRouter()

@router.post("", response_model=BlogRead)
def create_blog(
    payload: BlogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(UserRepository.get_current_user)
):
    blog_repo = BlogRepository(db=db)
    new_blog = blog_repo.create_blog(blog=payload, author_id=current_user.id)

    return new_blog

@router.get("", response_model=BlogPagination)
def get_blogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    blog_repo = BlogRepository(db=db)
    blogs = blog_repo.get_blogs(skip=skip, limit=limit)
    return blogs

@router.get("/{blog_id}", response_model=BlogSingleRead)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog_repo = BlogRepository(db=db)
    blog = blog_repo.get_blog(blog_id=blog_id)
    return blog

@router.put("/{blog_id}")
def update_blog(
    blog_id: int,
    payload: BlogUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(UserRepository.get_current_user)
):
    blog_repo = BlogRepository(db=db)
    blog_repo.update_blog(blog_id=blog_id, blog=payload, author_id=current_user.id)
    return {
        "success" : "Blog updated successfully"
    }

@router.delete("/{blog_id}")
def delete_blog(
    blog_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(UserRepository.get_current_user)
):
    blog_repo = BlogRepository(db=db)
    blog_repo.delete_blog(blog_id=blog_id, author_id=current_user.id)
    return {
        "success" : "Blog deleted successfully"
    }