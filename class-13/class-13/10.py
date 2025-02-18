def some(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    
    print(f"{n} -> {sum}")


def greet():
    print("Hello world")

def add(a, b):
    print(a+b)

def decorator(func):
    def wrapper(*args , **kwargs):
        print("Hi")
        func(*args, **kwargs)
        print("Finish")    
        print("-----------------------")
    return wrapper


my_decorator = decorator(some)

my_decorator(10)
my_decorator(20)


my_decorator_2 = decorator(add)
my_decorator_2(10 , 20)

my_decorator_3 = decorator(greet)
my_decorator_3()