def greet(value):
    if isinstance(value, int):
        value = value + 10
        return value
    
    if isinstance(value, str):
        value = "Hi " + value
        return value
    
    
    return "You type doesn't support!"


print( greet(10) )

print( greet("nahid") )

print( greet({"name" : "nahid"}) )
    