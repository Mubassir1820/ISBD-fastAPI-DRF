# from <module_name> import <variable1> , <function1> .... etc

from mock_2 import analysis_ratings

ls1 = [1, 2, 3, 4, 5]
ls2 = [3,5]
ls3 = None

print(f"Hello from {__name__}") # __main__

print(analysis_ratings(ls2))
print(analysis_ratings(ls1))
