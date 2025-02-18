def my_sum(*args):

    sum = 0
    for digit in args:
        sum = sum + digit

    return sum


print(my_sum(3, 5))
print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4))
print(my_sum(1, 2, 3, 4, 5))
print(my_sum(1, 2, 3, 4, 5, 6))
print(my_sum(1, 2, 3, 4, 5, 6, 7, 8))
print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# hw
# print(my_sum(1, 2, 3, 4, "a", "6", 7, 8, 9, 10))
