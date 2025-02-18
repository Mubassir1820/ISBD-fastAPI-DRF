from functools import partial

def calculate(base_number , power):
    return base_number ** power

squared = partial(calculate , power=2)
cubed = partial(calculate , power=3)

# square
print( squared(10) )
print( squared(20) )
print( squared(30) )

# cube
print( cubed(10) )
print( cubed(20) )
print( cubed(30) )


print(calculate(100 , 5))