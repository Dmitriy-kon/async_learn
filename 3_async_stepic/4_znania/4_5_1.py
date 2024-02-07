import asyncio

async def task(other):
    print(f"Ожидание задачи: {other.get_name()}")
    await other


async def main():
    task1 = asyncio.current_task()
    task2 = asyncio.create_task(task(task1))
    await task2
    

if __name__ == "__main__":
    asyncio.run(main())