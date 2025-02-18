def decorator(func):
    def wrapper(*args , **kwargs):
        print("Hi")
        func(*args, **kwargs)
        print("Finish")    
        print("-----------------------")
    return wrapper


@decorator
def some(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    
    print(f"{n} -> {sum}")

@decorator
def greet():
    print("Hello world")

@decorator
def add(a, b):
    print(a+b)


some(10)
some(15)

add(10, 20)

greet()