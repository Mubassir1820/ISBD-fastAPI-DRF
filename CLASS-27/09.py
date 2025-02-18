# Context Manager

class MyContext:
    def __init__(self) -> None:
        print("Constructor")

    def __enter__(self):
        print("enter")

    def __exit__(self, a, b, c):
        print("exit")

with MyContext() as ctx:
    print("------- here -------")