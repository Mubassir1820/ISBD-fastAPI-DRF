# "wraps" -> preserved function signature

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
        print("Hi")
        func(*args, **kwargs)
        print("Finish")    
        print("-----------------------")
    return wrapper


@decorator
def some(n):
    """ This is function , that gives the sum up to `n` """
    sum = 0
    for i in range(1,n+1):
        sum += i
    
    print(f"{n} -> {sum}")

# Function signature
print(some.__name__)
print(some.__doc__)