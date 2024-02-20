import asyncio


counter = 0

lock = asyncio.Lock()


async def worker_1():
    global counter

    # async with lock:
    for i in range(10):
        counter += 1
        print(f"Переменная counter из корутины worker_1 увеличилась и = {counter}")
        await asyncio.sleep(0.5)


async def worker_2():
    global counter

    # async with lock:
    for i in range(10):
        counter += 1
        print(f"Переменная counter из корутины worker_2 увеличилась и = {counter}")
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    await asyncio.gather(task1, task2)

    # await task1
    # await task2


if __name__ == "__main__":
    asyncio.run(main())
