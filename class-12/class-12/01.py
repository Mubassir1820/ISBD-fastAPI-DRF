# postional & keyword argument
def some(a, b, c):
    print(a, b, c)


# positional argument
some(1, 2, 3)

# keyword argument
some(a=1, b=2, c=3)

# postional , keyword
some(1, b=2, c=3)
some(1, 2, c=3)
some(1, c=3, b=2)

# wrong
# some(a=1,b=2, 3)
