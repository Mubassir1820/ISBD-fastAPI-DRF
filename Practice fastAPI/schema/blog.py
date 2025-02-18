from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from slugify import slugify
import time
from schema.user import UserView

class BlogRead(BaseModel):
    id: int
    slug: str
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class BlogCreate(BaseModel):
    title: str
    content: str
    is_active: bool = False
    slug: Optional[str] = None

    @classmethod
    def create_slug(cls, title: str) -> str:
        _slugify = slugify(title)
        _time_hash = hash(time.time())
        return f"{_slugify}-{_time_hash}"
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.title:
            self.slug = self.create_slug(self.title)



class BlogSingleRead(BaseModel):
    id: int
    slug: str
    content: str
    created_at: datetime
    author: UserView

    class Config:
        orm_mode = True

class BlogRead(BaseModel):
    id: int
    slug: str
    created_at: datetime
    author: UserView

    class Config:
        orm_mode = True

class BlogPagination(BaseModel):
    total_count: int
    skip: int
    limit: int
    data: List[BlogRead]

    class Config:
        orm_mode = True


class BlogUpdate(BaseModel):
   title: Optional[str] = None
   content: Optional[str] = None
   is_active: Optional[bool] = None
   slug: Optional[str] = None
   @classmethod
   def create_slug(cls, title: str) -> str:
       # Automatically generate a slug from the title
       _slugify = slugify(title)
       _time_hash = hash(time.time())
       return f"{_slugify}-{_time_hash}"
   # Override the `__init__` method to automatically generate the slug
   def __init__(self, **data):
       super().__init__(**data)
       if self.title:
           self.slug = self.create_slug(self.title)