# Function as an argument

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def quad(number):
    return number ** 4

def helper(function_name, number):
    return function_name(number)


result = helper(function_name=quad, number=5)

print(result)
