# from enum import Enum

# class Season(Enum):
#     SUMMER = 1
#     SPRING = 2
#     WINTER = 3
# print(Season.SUMMER)
# print(Season.SPRING.value)
# print(list(Season))


# while True:
#     try:
#         x = int(input("Please Enter a vaid Integer\n"))
#         print(x)
#         break
#     except ValueError:
#         print("Oops! Not an integer")


# from typing import Dict

# def get_salary(person: Dict):
#     sal = person['salary'] / person['tax']
#     return sal
    
# p = {
#     "salary": 30000,
#     "tax": 10
# }
# print("Starting")

# try:
#     get_salary(p)
# except Exception as e:
#     print(e)
    
    
# print("End")


# def process_entity(person: Dict):
#     cal = person['salary'] / person['tax']
#     return cal

# p = {
#     "salary": 1000,
#     "tax": 0
# }

# print("Before")

# try:
#     # dangerous code
#     process_entity(person=p)
# # except Exception as err:
# #     print(err)
# except ZeroDivisionError as e:
#     print("ZeroDivisionError", e)
# finally:
#     print("End of the program")
# print("After")


# filename = 'file_handling.txt'
# read_mode = 'r'

# f = open(filename, read_mode)

# # content = f.read()
# # print(content)
# # content = f.readline()
# # print(content)
# # content = f.readlines()
# # print(content)

# for each in f:
#     print(each)

# f.close()

# f = open('demo2.txt', 'w')

# f.write('This is a practice file')
# f.close()

# f = open('demo2.txt', 'a')

# f.write('This is a new line added by the appedn mode')

# f.close()


# Context manager

# class MyContext():
#     def __init__(self):
#         print("Program has started")

#     def __enter__(self):
#         print("Entering into the body phase")

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print("Program Ends")

# with MyContext() as ctx:
#     print("Main program body")

# class MyFileContext():
#     def __init__(self, filename,mode):
#         print("Constructor")
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         print("Context generated")
#         self.file = open(self.filename, self.mode)
#         return self.file
    
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print("Context Teardown")
#         self.file.close
    
# with MyFileContext(filename='demo.txt', mode='r') as file:
#     content = file.read()
#     print(content)


# Custom error class

class CustomError(Exception):
    # print("This is a custom error class")
    pass

try:
    x = int(input("Enter a number: "))
    if x < 10:
        raise CustomError
    else:
        print(x)
except CustomError:
    print("Invalid")