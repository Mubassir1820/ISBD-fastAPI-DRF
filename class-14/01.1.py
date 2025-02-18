from functools import singledispatch


@singledispatch
def greet(value):
    return "You type doesn't support!"

@greet.register(int)
def handle_int(value):
    value = value + 10
    return value

@greet.register(str)
def handle_str(value):
    value = "Hi " + value
    return value

print( greet(10) )

print( greet("nahid") )

print( greet({"name" : "nahid"}) )
    