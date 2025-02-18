# function with mutiple argument


def greet(name, email):
    print(f"Hello {name}. Your email is {email}")


greet(name="nahid", email="nahid@example.com")
greet(name="shakib", email="shakib@example.com")


greet("nahid@example.com", "nahid")
greet(email="nahid@example.com", name="nahid")
