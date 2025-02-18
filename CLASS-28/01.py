def greet(name:str):
    if not isinstance(name, str):
        raise ValueError("Name must be string")
    return "Hello " + name

greet(name="Nahid")
greet(name=10)