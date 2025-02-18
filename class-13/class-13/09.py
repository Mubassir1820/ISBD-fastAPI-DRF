def some(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    
    print(f"{n} -> {sum}")

def decorator(func):
    def wrapper(n):
        print("Hi")
        func(n)
        print("Finish")    
        print("-----------------------")
    return wrapper


my_decorator = decorator(some)


my_decorator(10)
my_decorator(20)
my_decorator(30)
my_decorator(40)


