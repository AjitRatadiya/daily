import asyncio


async def foo():
    print("1st")
    await asyncio.sleep(5)
    print("2nd")


async def hoo():
    task1 = asyncio.create_task(foo())
    print("hoo")
    task2 = asyncio.create_task(zoo())

    await asyncio.gather(task1, task2)


async def zoo():
    print("3rd")

    for a in range(5):
        print(a)
    await asyncio.sleep(1)
    print("4th")


asyncio.run(hoo())
