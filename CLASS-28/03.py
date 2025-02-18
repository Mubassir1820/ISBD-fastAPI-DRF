from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

def greet(person: Person) -> str:
    return "hello" + person.name



p1_dict = {
    "name": "Nahid",
    "age": 10
}

person = Person(**p1_dict)
greet(person=person)


# Pydantic examples