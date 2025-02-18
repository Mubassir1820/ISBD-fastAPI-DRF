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

    return 1

async def task2():
    print("task2 started")
    await sleep(3)
    print("task2 completed")

    return 2

async def task3():
    print("task3 started")
    print("task3 completed")

    return 3

async def call_my_funtion():
    print(datetime.now())
    # await asyncio.gather(task1(), task2(), task3())

    tasks = [
        task1(),
        task2(),
        task3()
    ]
    result =  await asyncio.gather(*tasks) # list unpacking
    print("result=" ,result)
    print(datetime.now())


print("Start")
asyncio.run(call_my_funtion())
print("End")