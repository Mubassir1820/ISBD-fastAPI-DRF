#db/base_class.py
import inflect
from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

# Create an inflect engine
p = inflect.engine()

@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        # Convert class name to lowercase and pluralize it
        singular_name = cls.__name__.lower()
        plural_name = p.plural(singular_name)
        return plural_name