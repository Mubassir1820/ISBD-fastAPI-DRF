# *args


def my_sum(*args):
    print(args, type(args))


my_sum(3, 5)
my_sum(1, 2, 3)
my_sum(1, 2, 3, 4)
my_sum(1, 2, 3, 4, 5)
my_sum(1, 2, 3, 4, 5, 6)
my_sum(1, 2, 3, 4, 5, 6, 7, 8)
