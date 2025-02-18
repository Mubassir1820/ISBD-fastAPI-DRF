# variable scope -> (global scope , function scope)

username = "abc"


def greet(username):
    global x
    global z

    x = 10

    y = 20

    z = 100
    print(username)

    return y


greet(username="DEF")

print(f"out of function ", username)

print(x)

# print(y) # error
