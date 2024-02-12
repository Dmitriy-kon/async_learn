import asyncio


async def task1():
    await asyncio.sleep(2)
    print("task1 за вершен")


async def task2():
    await asyncio.sleep(1)
    print("task2 за вершен")


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task1())
        tg.create_task(task2())


if __name__ == "__main__":
    asyncio.run(main())
