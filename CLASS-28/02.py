from pydantic import BaseModel

# pydantic model
class Person(BaseModel):
    Name: str
    age: int


# usage

p1 = Person(Name="Nahid", age=10)

print(p1.model_dump())

p1_dict = {
    "Name": "Nahid",
    "age": 10
}

# **p1_dict -> name = "Nahid" # Usage only in keyword argument

my_validation = Person(**p1_dict)
print(my_validation)




# CHeck for v1 and v2 pydantic