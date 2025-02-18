# A function returning a function

def outer():
    def inner():
        print("hello")
        return 100
    
    return inner

# print(outer()())

bairer_jayga = outer()

val = bairer_jayga()

print(val)








