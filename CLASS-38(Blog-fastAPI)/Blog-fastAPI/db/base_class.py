import inflect
from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

# Create an inflece engine
p = inflect.engine()

@as_declarative()
class Base:
    id: Any
    __name__: str


    # to generate table name from class name
    @declared_attr
    def __tablename__(cls) ->str:
        singular_name = cls.__name__.lower()
        plural_name = p.plural(singular_name)
        return plural_name