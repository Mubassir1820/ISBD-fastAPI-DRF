from time import sleep

def greet(name):
    print(f"for {name}")

    print("task - 1")
    print("task - 2")

    sleep(2)

    return f"hello {name}"


print( greet("nahid") )
print( greet("salman") )

print( greet("nahid") )
print( greet("nahid") )
print( greet("nahid") )
print( greet("salman") )
print( greet("salman") )
print( greet("nahid") )

print( greet("akib") )