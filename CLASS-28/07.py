# Asynchronus function / coroutine

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
    await task1()
    await task2()
    await task3()
    print(datetime.now())

asyncio.run(call_my_funtion())