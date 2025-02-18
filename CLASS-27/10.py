# Context Manager (File handling, db connection, redis connection)

class MyFileContext:
    def __init__(self, filename, mode) -> None:
        print("Constructor")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Context generated")
        self.file = open(self.filename, self.mode)
        return self.file

    # why these parameters important in exception handling
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Context tear down")
        self.file.close

with MyFileContext(filename='demo.txt', mode='r') as file:
    content = file.read()
    print(content)