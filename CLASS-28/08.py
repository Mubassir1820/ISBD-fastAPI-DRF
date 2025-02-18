"""
asyncio.gather(function_name1(), function_name2())
all functions should be async
"""

from datetime import datetime
import asyncio
from asyncio import sleep


async def task1():
    print("task1 started")
    await sleep(2)
    print("task1 completed")

async def task2():
    print("task2 started")
    await sleep(3)
    print("task2 completed")

async def task3():
    print("task3 started")
    print("task3 completed")

async def call_my_funtion():
    print(datetime.now())
    # await asyncio.gather(task1(), task2(), task3())

    tasks = [
        task1(),
        task2(),
        task3()
    ]
    await asyncio.gather(*tasks) # list unpacking
    print(datetime.now())


print("Start")
asyncio.run(call_my_funtion())
print("End")