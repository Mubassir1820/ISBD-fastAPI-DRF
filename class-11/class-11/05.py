# Optional parameter
def greet(name, email, age=None):
    if age is not None and isinstance(age, int) and age > 25:
        print("You are eligable")
    else:
        print("You are not eligable")

    print(f"Hello {name}. Your email is {email}")


greet(name="nahid", email="nahid@example.com")
greet(name="shakib", email="shakib@example.com", age="B")
greet(name="rakib", email="rakib@example.com", age=20)
greet(name="akib", email="akib@example.com", age=30)


# Variable data type check
# a = "10"
# print(isinstance(a, str))
# print(isinstance(a, int))
# print(isinstance(a, bool))
# print(isinstance(a, list))
# print(isinstance(a, dict))
