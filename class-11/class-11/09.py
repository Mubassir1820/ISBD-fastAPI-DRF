def calculate(number):
    square = number**2
    cube = number**3

    return square, cube


result_square, result_cube = calculate(number=10)

print(result_square)
print(result_cube)
