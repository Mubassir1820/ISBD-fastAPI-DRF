from db.base_class import Base
from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String
)


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean(), default=False)
    is_active = Column(Boolean(), default=True)
    image_url = Column(String, nullable=True)

