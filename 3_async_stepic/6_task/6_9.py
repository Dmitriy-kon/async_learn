import asyncio


async def main_task():
    print("main_task started")
    await asyncio.sleep(5)
    print("main_task finished")

async def main():
    task = asyncio.create_task(main_task())
    await asyncio.sleep(1)
    task.cancel()
    await asyncio.sleep(2)

    if task.cancelled():
        print("main_task was cancelled")

if __name__ == "__main__":
    asyncio.run(main())
