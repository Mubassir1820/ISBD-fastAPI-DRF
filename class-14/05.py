# Type Hint / Type annotation

def greet(name: str) -> str:
    return f"hello {name}"


greet()



def calculate(base_number: int | float, power: int | float) ->int | float:
    return base_number ** power

calculate(base_number=10, power=3)

# calculate(base_number="abc", power=10)
