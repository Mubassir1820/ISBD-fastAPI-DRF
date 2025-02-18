from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from db.models.blog import Blog
from schema.blog import BlogCreate, BlogPagination, BlogSingleRead, BlogUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


class BlogRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_blog(self, blog: BlogCreate, author_id: int) -> Blog:
        """
        Create a new Blog in the database.
        """
        db_blog = Blog(
            title=blog.title,
            slug=blog.slug,
            content=blog.content,
            is_active=blog.is_active,
            author_id=author_id
        )
        try:
            self.db.add(db_blog)
            self.db.commit()
            self.db.refresh(db_blog)
        except IntegrityError as e:
            print(e)
            self.db.rollback()
            raise HTTPException(status_code=400, detail=f"Something went wrong!")
        return db_blog
    

    def get_blogs(self, skip: int = 0, limit: int = 100) -> BlogPagination:
        """
        Retrieve a list of blogs with pagination.
        """

        total_count = self.db.query(func.count(Blog.id)).scalar()
        blogs = self.db.query(Blog).offset(skip).limit(limit).all()
        return BlogPagination(
            total_count=total_count,
            skip=skip,
            limit=limit,
            data=blogs
        )
    

    def get_blog(self, blog_id: int) -> BlogSingleRead:
        blog = self.db.query(Blog).filter(Blog.id == blog_id).first()
        if not blog:
            raise HTTPException(status_code=404, detail="Blog not found!")
        return blog
    

    def update_blog(self, blog_id: int, blog: BlogUpdate) -> Optional[Blog]:
        db_blog = self.db.query(Blog).filter(Blog.id == blog_id).first()
        if not db_blog:
            raise HTTPException(status_code=404,detail="Blog Not Found")
        
        if blog.title:
            db_blog.title = blog.title
            db_blog.slug = blog.slug

        if blog.content is not None:
            db_blog.content = blog.content

        if blog.is_active is not None:
            db_blog.is_active = blog.is_active

        self.db.commit()
        self.db.refresh(db_blog)
        return db_blog
    

    def delete_blog(self, blog_id: int) -> bool:

        db_blog = self.db.query(Blog).filter(Blog.id == blog_id).first()

        if not db_blog:
            raise HTTPException(status_code=404, detail="Blog not found!")
        self.db.delete(db_blog)
        self.db.commit()