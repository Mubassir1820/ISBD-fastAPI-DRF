# Synchronus functions

from datetime import datetime
from time import sleep


def task1():
    print("task1 started")
    sleep(2)
    print("task1 completed")

def task2():
    print("task2 started")
    sleep(3)
    print("task2 completed")

def task3():
    print("task3 started")
    print("task3 completed")


# Synchronus manner / approach
print(datetime.now())
task1()
task2()
task3()
print(datetime.now())


# WHat is event loop for python