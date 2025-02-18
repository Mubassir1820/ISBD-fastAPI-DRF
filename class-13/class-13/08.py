# Decorator with no parameter
def some():
    print("I am some function")


def decorator(func):
    def wrapper():
        print("Hi")
        func()
        print("Finish")    
    return wrapper


my_decorator = decorator(some)


my_decorator()
my_decorator()
my_decorator()
my_decorator()


